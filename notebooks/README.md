This directory contains the reader-friendly Jupyter notebooks displayed to the
user when they click the link to launch the current page in JupyterHub.

The directory `./generated/` contains machine-generated versions of the Jupyter
notebooks used as textbook pages, but with ugly directive cells removed.
Removing directive cells can be performed by running `make notebooks` in the
project root. This target is also run whenever the HTML version of the textbook
is built (using `make html`).

`./out_of_tree/` contains various other Jupyter notebooks that should be
available for interaction, but which are not themselves pages in the textbook.
They are not automatically generated.
