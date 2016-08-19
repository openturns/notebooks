#! /usr/bin/env python

from __future__ import print_function
import os
import sys
import glob
try:
    import nbformat
    import nbconvert
except ImportError:
    from IPython import nbformat
    from IPython import nbconvert

import traceback

current_path = os.path.dirname(os.path.realpath(__file__))
ipynb_path = current_path
ipynbs = [ipynb for ipynb in glob.glob(ipynb_path + '/*.ipynb')
          if 'skiptest' not in ipynb]

n_fail = 0
for ipynb in ipynbs:
    with open(ipynb) as fh:
        nb = nbformat.reads(fh.read(), 4)

    exporter = nbconvert.PythonExporter()

    # source is a tuple of python source code
    # meta contains metadata
    source, meta = exporter.from_notebook_node(nb)

    b_name = os.path.basename(ipynb)
    print('--', b_name)
    try:
        exec(source.encode())
        print('--', b_name, 'OK')
    except:
        n_fail += 1
        print('--', b_name, '***Failed')
        traceback.print_exc()

if n_fail > 0:
    sys.exit(1)
