# -*- coding: utf-8 -*-

import click
import os
from .base import BaseField

class ImageField(BaseField):
    filepath = ''

    def __init__(self, layout, canvas, data):
        super(ImageField, self).__init__(layout, canvas, data)

    def render(self):
        try:
            self._canvas.drawImage(
                    self.filepath, self.left, self.top, self.width, self.height)
        except IOError:
            click.secho('Unable to load image: %s' %
                    os.path.abspath(self.filepath))
