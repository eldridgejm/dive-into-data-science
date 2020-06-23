.. rst-class:: chapter-with-expand

.. _Accordion-DOCS:

*******************
Accordion Documents
*******************

This extension is to render documents that contain large sections using the
`accordion menu <http://jqueryui.com/accordion/>`_ technique. Each section in a
document is shown initially collapsed, and clicking on the title expands (and
collapses) its content. The initial paragraph in the page is left
expanded. This document is written with the accordion extension. The following
section describes how to achieve this behavior, and the rest (with no content)
are included to show how it works.

How to create an Accordion Doc
==============================

To have the sections behave as the accordion menu, simply add the following
directive to the top of the file::

  .. rst-class:: chapter-with-expand

Additionally, all sections that are preceded with the following marking::

  .. rst-class:: activity

will also be expanded/collapsed.


Another section
===============

Write your content here.

Another Section
===============

Write your content here.
