# -*- coding: utf-8 -*-

from stereo import Model
from stereo.fields import TextField

class NameField(TextField):
    font_name='Limelight'
    font_size=23
    fit_text=True
    text_align=TextField.TEXT_ALIGN_CENTER
    color='#222222'
    top=20
  #   width
  #   left

    def render(self):
        self.text = self.text.decode('utf-8').upper()

class RoleField(TextField):
    pass

class Badge(Model):
    input_file='guests.csv'
    template_file='template.pdf'
    output_dir='output'
    skip_first_row=True
    width=338
    height=338
    fields=[
        NameField(),
        RoleField()
    ]
    fonts={
        'Limelight': 'Limelight-Regular.ttf'
    }
