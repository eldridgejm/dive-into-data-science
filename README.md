Dive into Data Science
======================

*Dive into Data Science* is an introductory textbook which develops the core
ideas of statistics via programming and simulation instead of the manipulation
of mathematical formulae. At the same time, textbook does not assume that the
reader has any experience in programming; instead, we learn "just enough"
programming to do data science.  The textbook is written around the
[`babypandas`](https://github.com/babypandas-dev/babypandas) package; an
opinionated proper subset of the popular `pandas` package designed with the
novice data scientist in mind.


#### Table of Contents

- [Building](#building)
- [Developing](#developing)
    - [Getting Started](#getting-started)
    - [Project Structure](#project-structure)
    - [Extensions](#extensions)
    - [Reader-Friendly Jupyter Notebooks](#reader-friendly-jupyter-notebooks)
    - [Git Hooks](git-hooks)


Building
--------

The build is performed in a Docker container. No dependencies other than Docker
are needed.

To build the HTML version, run `make html` in the repository's root. To build a
PDF of the book, run `make pdf`.

On the first build of the book, the Docker image will also be built -- this
may take several minutes. Subsequent builds of the book will be much faster.


Developing
----------

### Getting Started

Before working on the book, run `make init` in the project's root. This will
build the Docker image used for compiling the textbook, install git commit
hooks, etc.

### Project Structure

This textbook is written using [JupyterBook](jupyterbook.org) along with
several custom extensions and scripts.

The `book/` directory contains the book's contents. `book/_config.yml` contains
important configuration variables, such as the URL of the JupyterHub that will
be used to launch notebooks interactively.

`extensions/` contains the extensions which define custom directives. See
"Extensions" below.

`notebooks/` contains machine-generated versions of the Jupyter notebooks used
as textbook pages, but with ugly directive cells removed. Removing directive
cells can be performed by running `make notebooks` in the project root. This
target is also run whenever the HTML version of the textbook is built (using
`make html`).

`scripts/` contains various scripts used in the development and building of the
textbook. These scripts should generally not be invoked manually.

### Extensions

Several extensions of MyST are used in this textbook.

#### The "hiddenanswer" directive

This directive provides a way of quickly "quizzing" readers for understanding.
It is invoked as follows:

    ```{hiddenanswer}
    ---
    question: This is the question.
    answer: This is the answer.
    ```

This will create a "tabbed" container. The first tab will show the question.
Clicking on the second tab shows the answer.

Long answers or code can be included using the proper YAML syntax:

    ````{hiddenanswer}
    ---
    question: |
        This is the question,
        which will be
        1. Parsed *as* [MyST](#)
        2. With paragraph breaks preserved

        Like this.
    answer: |
        ```
        def func(arg):
            return 42
        ```
    ````
(note that an additional backtick is used in the directive code fence to allow us to nest a code block in the answer)

#### The "jupytertip" and "jupytertiplist" directives

The `jupytertip` directive creates an admonition box intended to display a tip
related to Jupyter notebooks. The `jupytertiplist` directive creates list of
all of the tips.

Example:

    ```{jupytertip}

    Select `Kernel -> Restart and Run All` to restart the kernel and run all of
    the notebook's cells from top to bottom.
    ```

### Reader-Friendly Jupyter Notebooks

Much of the textbook is written in Jupyter Notebooks which are then converted to
HTML by the build process. Readers can click the rocket icon to launch the
notebook version of the given page in a JupyterHub session.

However, the Jupyter notebooks used as source documents may include directives
and other content that might confuse readers. Therefore, as part of the build
process, the source notebooks are transformed into "reader-friendly" notebooks
and stored in the `notebooks/` directory (these are the notebooks that are
launched when the user clicks the rocket link to interact with a page). The
notebooks are made "reader-friendly" by several mechanisms:


#### Admonition Cells

Cells containing an admonition, such as

    ```{warning}

    This is a warning.
    ```

are automatically-identified and converted to Markdown:

    **Warning**

    This is a warning.


This conversion occurs only if the directive is the only content of the cell.
See `./scripts/make_reader_friendly_notebooks.py` for more information.


#### Hiddenanswer Cells

Cells containing a hidden answer directive, such as

    ```{Hiddenanswer}
    ---
    question: This is the question
    answer: This is the answer
    ```

are automatically-identified and converted to Markdown:

    **Question**: This is the question

    **Answer**: This is the answer

This conversion occurs only if the directive is the only content of the cell.
See `./scripts/make_reader_friendly_notebooks.py` for more information.


#### Hiding Cells

Cells can be hidden in the reader-friendly version by adding a
`hide-from-reader` tag to the cell.

### Git Hooks

To install the Git hooks, run `make init` in the repository root.

The pre-commit hook removes the output of every cell in every notebook in
`book/`. This makes for more meaningful diffs.
