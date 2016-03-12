import stereo

class NameField(stereo.TextField):
    font_name='Limelight'
    font_size=23
    fit_text=True
    text_align=stereo.TextField.TEXT_ALIGN_CENTER
    color='#222222'
    top=20
  #   width
  #   left

    def render(self):
        self.text = self.text.decode('utf-8').upper()

class RoleField(stereo.TextField):
    pass

class Badge(stereo.Document):
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
