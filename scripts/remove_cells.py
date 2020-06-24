"""
Given a path to a directory containing Jupyter notebooks, copies all of the
notebooks to the current working directory, removing cells tagged "remove_cell"
in the process.
"""

import argparse
import pathlib

from traitlets.config import Config
from nbconvert.exporters import NotebookExporter
import nbformat


REMOVE_CELL_TAG = 'remove_cell'


def source_notebooks(src):
    """Yield all of the notebooks not in the _build or .ipynb_checkpoints directories."""
    for path in src.glob('**/*.ipynb'):
        if '_build' not in path.parts and '.ipynb_checkpoints' not in path.parts:
            yield path


def remove_cells(src_notebook):
    """Given a path to a source notebook, removes all cells with REMOVE_CELL_TAG as a tag."""
    c = Config()
    c.TagRemovePreprocessor.remove_cell_tags = [REMOVE_CELL_TAG]
    c.NotebookExporter.preprocessors = ['nbconvert.preprocessors.TagRemovePreprocessor']
    notebook, resources = NotebookExporter(config=c).from_filename(src_notebook)
    return notebook


def replicate_source_without_cells(src, dst):
    """Replicate the source directory notebooks, but filtering out cells.

    Arguments
    ---------
    src : pathlib.Path
        The path to the source directory that should be searched.
    dst : pathlib.Path
        The path to the directory where the replicated notebooks will be placed.

    """
    for src_notebook in source_notebooks(src):
        notebook_code = remove_cells(src_notebook)
        dst_notebook = dst / (src_notebook.relative_to(src))

        dst_notebook.parent.mkdir(parents=True, exist_ok=True)

        with dst_notebook.open('w') as fileobj:
            fileobj.write(notebook_code)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('src', type=pathlib.Path)
    args = parser.parse_args()

    replicate_source_without_cells(args.src, pathlib.Path.cwd())
