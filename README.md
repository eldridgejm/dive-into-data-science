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


Building
--------

The build is performed in a Docker container. No dependencies other than Docker
are needed.

To build the HTML version, run `make html` in the repository's root. To build a
PDF of the book, run `make pdf`.

The Makefile assumes that you are running on a Unix-like operating system, and
that your UID is 1000 (this can be checked by running `id -u` in a terminal). If
this is not the case, you will need to rebuild the Docker image in order to
avoid permissions issues. This can be done by issuing `make docker` once. After
this image is built, you will not need to build it again.
