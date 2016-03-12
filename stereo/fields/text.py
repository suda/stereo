# -*- coding: utf-8 -*-

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import enums
from reportlab.platypus import Paragraph

class TextField():
    TEXT_ALIGN_LEFT=enums.TA_LEFT
    TEXT_ALIGN_CENTER=enums.TA_CENTER
    TEXT_ALIGN_RIGHT=enums.TA_RIGHT
    TEXT_ALIGN_JUSTIFY=enums.TA_JUSTIFY

    font_name=None
    font_size=0
    fit_text=True
    text_align=TEXT_ALIGN_LEFT
    color='#000000'
    top=0
    left=0
    width=0
    height=0

    def __init__(self, model, canvas, data):
        self._model = model
        self._canvas = canvas
        self.data = data

        if self.width == 0:
            self.width = self._model.width

    def render(self):
        style = getSampleStyleSheet()['Normal']
        style.alignment = self.text_align
        style.fontSize = self.font_size
        style.fontName = self.font_name

        p = Paragraph('<font color="%s">%s</font>' % (self.color, self.data), style)
        p.wrap(self.width, self.height)
        p.drawOn(self._canvas, self.left, self._model.height-self.top)
