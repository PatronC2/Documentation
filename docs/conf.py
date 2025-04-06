import os
import sys
sys.path.insert(0, os.path.abspath('..'))

html_theme = 'sphinx_rtd_theme'

extensions = [
    'myst_parser',
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

project = 'Patron C2'
author = 'Patron C2'
release = os.environ.get("READTHEDOCS_VERSION", "local")
