# -*- coding: utf-8 -*-

class BaseField():
    top=0
    left=0
    width=0
    height=0

    def __init__(self, layout, canvas, data):
        self._layout = layout
        self._canvas = canvas
        self.data = data

    def render(self):
        pass
