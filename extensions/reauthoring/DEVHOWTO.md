# Reauthoring: A Toolkit to create Liquid HTML Active Learning Resources

This document explains the initial steps to extend the functionality in Reauthoring to include additional directives and their corresponding code.

The most important step is first to get familiar with how Sphinx-doc and ReStructuredText are combined to generate documentation as self-contained web sites. Once you understand what the tool does and how it does it, read the documentation on `Developing extensions for Sphinx <http://www.sphinx-doc.org/en/stable/extdev/index.html>`_. Extensions are simply Python modules, and they require the definition of certain classes and functions so that they are invoked at the right time while processing the source files.

Start by replicating the work in the section `Tutorial: Writing a simple extension <http://www.sphinx-doc.org/en/stable/extdev/tutorial.html>`__. Make sure you understand the classes that are used and how to define the event handlers. Modify this initial simple extension to include the functionality you need.

Happy directive hacking!
