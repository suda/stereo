# -*- coding: utf-8 -*-

import os, sys, inspect
from importlib import import_module
import six, click

def _import_file(filepath):
    abspath = os.path.abspath(filepath)
    dirname, file = os.path.split(abspath)
    fname, fext = os.path.splitext(file)
    if fext != '.py':
        raise ValueError("Not a Python source file: %s" % abspath)
    if dirname:
        sys.path = [dirname] + sys.path
    try:
        module = import_module(fname)
    finally:
        if dirname:
            sys.path.pop(0)
    return module

def _iter_layout_classes(module):
    from stereo import Layout

    for obj in six.itervalues(vars(module)):
        if inspect.isclass(obj) and \
           issubclass(obj, Layout) and \
           obj.__module__ == module.__name__:
            yield obj

def generate(filename, data_file, output_dir, template_file, skip_first_row):
    if not os.path.exists(filename):
        raise click.UsageError("Layout not found: %s\n" % filename)
    try:
        module = _import_file(filename)
    except (ImportError, ValueError) as e:
        raise click.UsageError("Unable to load %r: %s\n" % (filename, e))
    layout_classes = list(_iter_layout_classes(module))
    if not layout_classes:
        raise click.UsageError("No layout found in file: %s\n" % filename)
    layout_cls = layout_classes.pop()
    layout = layout_cls(data_file, output_dir, template_file, skip_first_row)
    layout.run()
