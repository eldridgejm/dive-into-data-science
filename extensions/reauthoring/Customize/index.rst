****************************
How to Customize these Pages
****************************

The main source of customization for these pages is the file ``conf.py``
located at the root of the repository. The variables and values are described
in the `build configuration file
<http://sphinx-doc.org/config.html#build-config>`_ description.

Once you have the file in your local machine, you can tweak its values to your
linking. You may generate a similar file for a new project using the
`sphinx-quickstart <http://sphinx-doc.org/man/sphinx-quickstart.html>`_
command.

There are four other sources of customization that you can explore:

1. CSS styles: The folder ``_static`` contains CSS files defining the style for
   the created HTML. For example, the logo that appears in the left corner of
   the side menu is taken from the file `logo.png <../_static/logo.png>`_ in
   this folder. You may replace this file with your own logo and all pages will
   show it.

2. Javascript files: In the same folder ``_static`` you will also find
   javascript files that support the active components in the pages.

3. ``Sphinx_ext``: This folder contains python code that is added to Sphinx to
   provide support for the additional directives.

4. ``_templates``: This folder contains the HTML skeleton to generate the
   pages. Modify these files to reshape the overall structure of the page.

Use Reauthoring as a submodule of your project
==============================================

If instead of using this whole project as your template you prefer to create
your own and still use some of the features provided by Reauthoring, you may
achieve this using `git <http://git-scm.com/>`_ and performing a *sparse
checkout*. In simple terms, you may checkout only three folders from
Reauthoring as subfolders in your Sphinx project. This way, you can keep up
with new versions for the templates, styles, javascripts and extensions.

