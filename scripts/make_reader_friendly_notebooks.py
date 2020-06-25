"""
Generate the "reader friendly" version of a notebook used as a textbook source document.

Notebooks used as source documents may have content that is confusing to readers,
such as directives or visible cell tag toolbars. This script cleans all of these
up and generates new notebooks that are "reader friendly".

Usage
-----
    python make_reader_friendly_notebooks.py src_directory

This recursively search and find all of the notebooks under src_directory,
placing its output in the current directory in a way that mimics the directory
structure of the source directory.

This script is invoked by the `notebooks` target in the Makefile at the root of
the directory. It does not need to be invoked manually.
"""

# configuration
# ======================================================================================

# directories that should not be searched for notebooks
EXCLUDED_FROM_SEARCH = {'_build', '.ipynb_checkpoints'}

# cells with these tags will be hidden from the reader
HIDE_CELL_TAGS = {'hide-from-reader'}


# ======================================================================================

import argparse
import pathlib
import yaml
import re

from traitlets.config import Config
from nbconvert.exporters import NotebookExporter
import nbformat


# hiding cells
# ======================================================================================
# code for hiding some of the notebook's cells from the reader

def hide_cells(notebook):
    """Removes all cells with tags in HIDE_CELL_TAGS. Modifies notebook in-place."""
    # we can't directly delete cells from the notebook node
    # instead, we'll build a new list of cells without the cells being filtered out
    # and replace the old cells with this new list in the node
    new_cells = []
    for cell in notebook['cells']:
        try:
            tags = set(cell['metadata']['tags'])
        except KeyError:
            tags = set()

        if not tags.intersection(HIDE_CELL_TAGS):
            new_cells.append(cell)

    notebook['cells'] = new_cells


# cleaning toolbars
# ======================================================================================
# code for cleaning up cell toolbars

def clear_cell_toolbars(notebook):
    """Removes everything from the cell toolbar."""
    if 'celltoolbar' in notebook['metadata']:
        del notebook['metadata']['celltoolbar']


# transforming
# ======================================================================================
# code for transforming cells so that they appear nicer to the reader

# we will most often want to transform cells containing directives. For instance, we
# will want to take a cell containing:
#
#   ```{warning} this is a warning```
#
# and turn it into something nicer for the reader. We can easily identify directive cells
# by inspecting their first line for a directive. We can then perform the appropriate 
# transformation.

# we'll do this by having a different transformation function for each directive. A transformation
# function takes in a cell and modifies its source. We'll register these
# transformers with a decorator:

DIRECTIVE_TRANSFORMERS = dict()


def directive_transformer(directives):
    """A decorator for associative a transformer with the directives it transforms."""
    def decorator(wrapped):
        for directive in directives:
            DIRECTIVE_TRANSFORMERS[directive] = wrapped
        return wrapped
    return decorator


def remove_directive_markup(source):
    """Removes the beginnning ```{} and ending ``` from the source."""
    # remove the starting markup
    source = re.sub('^`{3,}\{.+\}', '', source)
    # remove the ending markup
    source = re.sub('`{3,}$', '', source)
    return source.strip()


def find_directive_cells(notebook):
    """Finds all cells starting with a directive."""
    for cell in notebook['cells']:
        all_directives = re.findall('`{3,}\{(.+)\}', cell['source'])

        if len(all_directives) == 1:
            directive = all_directives[0]
            yield directive, cell
        else:
            continue


def transform_cells_by_directive(notebook):
    """Transforms cells whose first line is a recognized directive."""
    for directive, cell in find_directive_cells(notebook):
        if directive in DIRECTIVE_TRANSFORMERS:
            transformer = DIRECTIVE_TRANSFORMERS[directive]
            transformer(directive, cell)


# admonition directives
# --------------------------------------------------------------------------------------
# we'll start with a transformer for admonitions. here are the built-in admonitions:


ADMONITION_DIRECTIVES = {
        'danger', 'error', 'warning', 'caution', 'attention', 'important', 'note', 'hint',
        'tip', 'seealso', 'jupytertip'}

# when we transform an admonition, we'll want to place a header like "Warning" in the
# reader-friendly notebook. Most of these admonitions have names which can serve as headers
# (after title-casing them). Some need special treatment:

HEADERS = {
    'jupytertip': 'Jupyter Tip',
    'seealso': 'See Also'
}


@directive_transformer(ADMONITION_DIRECTIVES)
def transform_admonition_directive(directive, cell):
    """Transform a cell containing an admonition.

    Transforms a cell containing something like:

       ```{warning}

       Oh no! Watch out!
       ```

    to this Markdown:

        ***Warning***

        Oh no! Watch out!

    """
    source = remove_directive_markup(cell['source'])

    if directive in HEADERS:
        header = HEADERS[directive]
    else:
        header = directive.title()

    # we'll transform this to some basic markdown
    cell['source'] = f"**{header}**\n\n{source}"


# hiddenanswer directives
# -----------------------

@directive_transformer({'hiddenanswer'})
def transform_hiddenanswer_directive(directive, cell):
    """Transforms a cell containing a hiddenanswer directive.

    Takes this:

        ```{hiddenanswer}
        ---
        question: This is the question
        answer: This is the answer
        ```

    and turns it into this:

        **Question**: This is the question
        **Answer**: This is the answer

    """
    source = remove_directive_markup(cell['source'])
    content = yaml.load(source, Loader=yaml.Loader)
    cell['source'] = f"**Question**:\n {content['question']}\n\n<details><summary><b>Answer</b>:</summary>{content['answer']}</details>"


# i/o
# ======================================================================================
# functions useful for finding, writing, and reading notebooks

def find_notebooks(src_directory):
    """Yield paths of all the notebooks not in a EXCLUDED_FROM_SEARCH directory."""
    for path in src_directory.glob('**/*.ipynb'):
        if not any(d in path.parts for d in EXCLUDED_FROM_SEARCH):
            yield path


def read_notebook(path):
    """Returns a notebook node from a path."""
    with path.open() as fileobj:
        return nbformat.read(fileobj, as_version=4)


def write_notebook(path, notebook):
    """Writes a notebook node to the path."""
    notebook_code, resources = NotebookExporter().from_notebook_node(notebook)
    with path.open('w') as fileobj:
        fileobj.write(notebook_code)


# main
# ======================================================================================

def make_reader_friendly_notebooks(src_directory, dst_directory):
    """Search for notebooks and make them reader friendly.

    Arguments
    ---------
    src_directory : pathlib.Path
        The path to the source directory that should be searched.
    dst_directory : pathlib.Path
        The path to the directory where the processed notebooks will be placed.

    """
    for notebook_path in find_notebooks(src_directory):
        notebook = read_notebook(notebook_path)

        hide_cells(notebook)
        transform_cells_by_directive(notebook)
        clear_cell_toolbars(notebook)

        friendly_notebook_path = dst_directory / (notebook_path.relative_to(src_directory))
        friendly_notebook_path.parent.mkdir(parents=True, exist_ok=True)
        write_notebook(friendly_notebook_path, notebook)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('src_directory', type=pathlib.Path)
    args = parser.parse_args()

    make_reader_friendly_notebooks(args.src_directory, pathlib.Path.cwd())
