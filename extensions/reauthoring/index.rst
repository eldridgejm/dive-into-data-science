
######################################################################
Reauthoring: A Toolkit to create Liquid HTML Active Learning Resources
######################################################################

.. figure:: Images/team_michael_cardus_flickr.jpg
   :width: 150px
   :target: https://www.flickr.com/photos/create-learning/9351356386
   :alt: Team Work
   :figclass: align-left reference

   `Michael Cardus <https://www.flickr.com/photos/create-learning/9351356386>`_

Reauthoring is a toolkit that processes documents written in `reStructuredText
<http://sphinx-doc.org/rest.html>`_ using `sphinx-doc <http://sphinx-doc.org>`_
with a set of extensions specifically designed to create learning content. The
result is a folder (``_build/html``) with a self-contained web site where you
can see the files with your browser. Once you are happy about the content,
simply copy it to your Learning Management System (LMS) and it is ready to use.

The HTML files are rendered with the `Sphinx Read the Docs Theme
<http://docs.readthedocs.org/en/latest/theme.html>`_ which provides a rendering
that adapts to mobile devices. Once you make this documentation available in a
server, make sure you check it with a phone or a tablet.

The functionality provided by `sphinx <http://sphinx-doc.org>`_ has been
extended with directives to create common elements in a learning
environment. The links at the bottom of this document explain these extensions
and how to use them.

You can also use this document (and its sub-pages) as a template for your own
project. First read about :ref:`Reauthoring-INSTALL`. Then read about how to
use `Sphinx <http://sphinx-doc.org>`__ and then re-purpose the files to your
needs and create your own course notes. Any page has a link to the source file,
that is, the document given to Sphinx to transform it into the HTML you are
seeing. Go ahead and *Feel the source, Luke*.

.. toctree::
   :maxdepth: 2

   /install
   /Embedded_questions/index
   /Videos/index
   /Sequences/index
   /Activity/index
   /2D_rank/index
   /Accordion_docs/index
   /Customize/index

Drop us a note telling us what you think about the toolkit `by creating an
issue in our issue tracker
<https://bitbucket.org/abelardopardo/reauthoring/issues/new>`_.

