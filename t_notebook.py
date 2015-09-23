#! /usr/bin/env python

from __future__ import print_function
import os
import glob
import nbformat
from nbconvert import PythonExporter
import traceback

current_path = os.path.dirname(os.path.realpath(__file__))
ipynb_path = current_path
ipynbs = glob.glob(ipynb_path + '/*.ipynb')

for ipynb in ipynbs:
    with open(ipynb) as fh:
        nb = nbformat.reads(fh.read(), 4)

    exporter = PythonExporter()

    # source is a tuple of python source code
    # meta contains metadata
    source, meta = exporter.from_notebook_node(nb)

    b_name = os.path.basename(ipynb)
    print('--', b_name)
    try:
        exec(source.encode())
        print('--', b_name, 'OK')
    except:
        print('--', b_name, '***Failed')
        traceback.print_exc()
