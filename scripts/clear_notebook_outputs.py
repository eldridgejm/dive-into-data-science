"""Recursively searches for notebooks and clears the output of every cell.

This script is used as a Git pre-commit hook.
"""

import pathlib

from traitlets.config import Config
from nbconvert.exporters import NotebookExporter
import nbformat


def clear_outputs(notebook_path):
    c = Config()
    c.NotebookExporter.preprocessors = ['nbconvert.preprocessors.ClearOutputPreprocessor']
    notebook, resources = NotebookExporter(config=c).from_filename(notebook_path)

    with notebook_path.open('w') as fileobj:
        fileobj.write(notebook)


if __name__ == '__main__':
    for notebook_path in pathlib.Path.cwd().glob('**/*.ipynb'):
        clear_outputs(notebook_path)
