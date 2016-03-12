# -*- coding: utf-8 -*-

import click
from . import generator

@click.group()
def default():
    pass

@default.command()
@click.argument('model')
@click.option('-d', '--data-file', help='CSV file used to generate documents')
@click.option('-o', '--output-dir', default='output', help='Directory where to store generated documents')
@click.option('-t', '--template-file', help='PDF file used as template')
@click.option('-s', '--skip-first-row', default=True, help='Skip the first row in CSV file?')
def generate(model, data_file, output_dir, template_file, skip_first_row):
    """
    Generate documents based on MODEL file
    """
    generator.generate(model, data_file, output_dir, template_file, skip_first_row)
