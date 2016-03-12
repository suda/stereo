# -*- coding: utf-8 -*-

import os
import csv
import hashlib
import click, six
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PyPDF2 import PdfFileWriter, PdfFileReader

try:
    from StringIO import StringIO
except ImportError:
    from io import BytesIO as StringIO

class Layout():
    data_file=None
    template_file=None
    output_dir=None
    skip_first_row=True
    width=0
    height=0
    fields=[]
    fonts={}
    debug_fields=False

    def __init__(self, data_file, output_dir, template_file, skip_first_row):
        # Override layout defaults
        if data_file:
            self.data_file = data_file
        if output_dir:
            self.output_dir = output_dir
        if template_file:
            self.template_file = template_file
        if skip_first_row:
            self.skip_first_row = skip_first_row

    def _init_pdf(self):
        # Register fonts
        for name, filename in six.iteritems(self.fonts):
            click.secho('  Registering %s as %s' % (filename, name), fg='cyan')
            pdfmetrics.registerFont(TTFont(name, filename))

    def _check_paths(self):
        if not os.path.exists(self.data_file):
            raise click.UsageError("Data file not found: %s\n" % self.data_file)
        if not os.path.exists(self.template_file):
            raise click.UsageError("Template file not found: %s\n" % self.template_file)
        if os.path.exists(self.output_dir) and not os.access(self.output_dir, os.W_OK):
            raise click.UsageError("Output is not writable: %s\n" % self.output_dir)

    def generate_filename(self, row):
        m = hashlib.md5()
        m.update(''.join(row).encode('utf-8'))
        return str(m.hexdigest())

    def generate_row(self, row):
        packet = StringIO()
        template = PdfFileReader(open(self.template_file, 'rb'))
        c = canvas.Canvas(packet, pagesize=(self.width, self.height))

        i = 0
        for field_cls in self.fields:
            # TODO: Catch exception if there is less columns than fields
            field = field_cls(self, c, row[i])
            field.render()
            i += 1

        # Save canvas
        c.save()
        packet.seek(0)
        text = PdfFileReader(packet)
        output = PdfFileWriter()
        # Merge text with base
        page = template.getPage(0)
        page.mergePage(text.getPage(0))
        output.addPage(page)

        # Save file
        filename = "%s/%s.pdf" % (self.output_dir, self.generate_filename(row))
        outputStream = open(filename, 'wb')
        output.write(outputStream)
        outputStream.close()

    def run(self):
        # Check files/paths
        self._check_paths()

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        # TODO: Use logging
        click.secho('Generating documents...', fg='white')

        # Init PDF generator
        self._init_pdf()

        self._data = csv.reader(open(self.data_file))
        if self.skip_first_row:
            next(self._data)

        # TODO: Show info about rows count
        for row in self._data:
            self.generate_row(row)
