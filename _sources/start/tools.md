Tools of the Trade
==================

It 2019 it was estimated[^domo] that, in any given minute,
188 million emails are sent, 55 thousand images are posted to Instagram, and
4.5 million YouTube videos are watched. All of this digital activity generates
massive amounts of data, and it's a data scientist's job to analyze it.
Of course, any data set of moderate size cannot be analyzed with pencil and
paper alone; instead, we turn to computers to do the heavy lifting. In this
textbook, we will learn several of the most important computational tools used
by working data scientists *today*: *Python*, *Jupyter notebooks*, and the *Pandas*
data science package.

In order to utilize the full power of a computer to run an analysis, we'll need
to know the basics of a good programming language. By far, the most popular[^kaggle]
programming language among data scientists is
[Python](http://www.python.org). While other languages tend to be verbose and
formal, Python is relatively easy-going. In this textbook, we'll learn just
enough Python to do interesting things with data.

```{figure} ../images/python-logo.png
---
height: 100px
---
```

The type of computer programming done by data scientists is quite different from
that done by a software engineer building the latest and greatest word
processor. We write code in order to explore data sets in a process that is
anything but linear. For instance, given a data set listing the salary of every
city employee, our first question is probably: What is the highest salary? We'll
soon see that this can be answered with a short piece of Python code. Next, we
might ask *who* has the highest salary This, too, is answered by a small piece
of code. And so on. We ask a question, write some code, and interpret the
result. Our next question depends on the answer to the last.  We use a computer
like it is a very powerful calculator.

Because the type of programming done by data scientists is unique, we use a
unique tool to write and run our code: [Jupyter
notebooks](https://jupyter.org/). A Jupyter notebook is a mosaic of code, text,
HTML, images, videos and more that can be edited and executed *right in the
browser*.  Notebooks are like advanced calculators, in the sense that the user
can write a piece of code, run it, and see the result below. Many of the pages
in this textbook are written in Jupyter Notebooks, and you will be able to click
a button to open the notebook and interact with the code on the page (even
editing it, if you want).

```{figure} ../images/jupyter-logo.svg
---
height: 150px
---
```

Python is a powerful *general purpose* programming language, meaning that it
isn't designed for data science in particular. In fact, Python is popularly used
for writing web applications (the behind-the-scenes code that runs Reddit is
entirely written in Python). By itself, Python doesn't come with the
functionality that data scientists need. Luckily, Python -- like all major
programming languages -- can be extended by installing **packages** which
provide additional capabilities.

Without a doubt, the most important Python package used by data scientists is
[pandas](http://pandas.pydata.org). Pandas is an immensely powerful tool for
exploring and manipulating large data sets.  But with great power comes great
complexity. There are several ways to perform even the simplest tasks using
Pandas, making it a difficult tool to learn.

For this reason, we have designed a simplified version of pandas, which
we are calling *babypandas*. Babypandas is a *subset* of pandas, meaning that we
have carefully taken some of the pieces of pandas, but left out much of it.
We'll be using babypandas throughout this book. Remember: learning how to use
babypandas is actually learning how to use pandas, and all of the code you see
in this textbook uses the same tools that working data scientists are using
every day.

```{figure} ../images/babypandas-logo.jpg
---
height: 150px
---
```



[^domo]: <a href="https://www.domo.com/learn/data-never-sleeps-7" target="_blank">https://www.domo.com/learn/data-never-sleeps-7</a>
[^kaggle]: <a href="https://www.kaggle.com/kaggle/kaggle-survey-2018" target="_blank">https://www.kaggle.com/kaggle/kaggle-survey-2018</a>
