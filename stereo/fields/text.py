# -*- coding: utf-8 -*-

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import enums
from reportlab.platypus import Paragraph
from reportlab.pdfbase.pdfmetrics import stringWidth
from .base import BaseField

class TextField(BaseField):
    TEXT_ALIGN_LEFT = enums.TA_LEFT
    TEXT_ALIGN_CENTER = enums.TA_CENTER
    TEXT_ALIGN_RIGHT = enums.TA_RIGHT
    TEXT_ALIGN_JUSTIFY = enums.TA_JUSTIFY

    font_name = None
    font_size = 0
    fit_text = True
    text_align = TEXT_ALIGN_LEFT
    color = '#000000'

    def __init__(self, layout, canvas, data):
        super(TextField, self).__init__(layout, canvas, data)
        self._offset_top = 0

        if self.width == 0:
            self.width = self._layout.width

    def render(self):
        style = getSampleStyleSheet()['Normal']
        style.alignment = self.text_align
        style.fontName = self.font_name
        if self._layout.debug_fields:
            style.backColor = "rgba(255, 0, 0, 0.5)"

        if self.fit_text:
            original_size = self.font_size
            text_width = stringWidth(self.data, self.font_name, self.font_size)
            while text_width > self.width:
                self.font_size -= 1
                text_width = stringWidth(self.data, self.font_name, self.font_size)
            # Size has been adjusted. Lower text accordingly
            if original_size > self.font_size:
                self._offset_top = (original_size - self.font_size) / 2.0

        if self.height == 0:
            self.height = self.font_size
        style.fontSize = self.font_size
        style.leading = self.font_size


        p = Paragraph('<font color="%s">%s</font>' % (self.color, self.data), style)
        p.wrap(self.width, self.height)
        top = self._layout.height - self.top - self.height - self._offset_top
        p.drawOn(self._canvas, self.left, top)
