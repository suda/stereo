# -*- coding: utf-8 -*-

from stereo import Model
from stereo.fields import TextField

class NameField(TextField):
    font_name='Limelight'
    font_size=23
    fit_text=True
    text_align=TextField.TEXT_ALIGN_CENTER
    color='#222222'
    top=60

    # def render(self):
    #     self.text = self.text.decode('utf-8').upper()

class RoleField(TextField):
    font_name='Limelight'
    font_size=14
    fit_text=True
    text_align=TextField.TEXT_ALIGN_CENTER
    color='#222222'
    top=85

class Badge(Model):
    data_file='guests.csv'
    template_file='template.pdf'
    output_dir='output'
    skip_first_row=True
    width=258
    height=173
    fields=[
        NameField,
        RoleField
    ]
    fonts={
        'Limelight': 'Limelight-Regular.ttf'
    }

    def generate_filename(self, row):
        return str(row[0]).replace(' ', '-').strip()
