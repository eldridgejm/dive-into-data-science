.. _Reauthoring-INSTALL:

Installing Reauthoring
======================

1) Install Python (2.7.9) and Sphinx (latest version)

   `Install Python and Sphinx <http://sphinx-doc.org/latest/install.html>`_

#) Install the sphinx_rtd_theme

   Open a command window and type::

     pip install sphinx_rtd_theme

   You may check the `instructions to install Sphinx RTD Theme
   <https://github.com/snide/sphinx_rtd_theme>`_

#) Install additional required python packages

   Open a command window, make sure you are in the root folder of this project and
   type::

     pip install -r requirements.txt

#) Create an initial project

   For this step we are going to use the this project as a sample.

   1. Go to https://bitbucket.org/abelardopardo/reauthoring/downloads
  
   2. Download the repository. 
  
   3. Unpack the ZIP in a folder. Alternatively to these three steps you can
      clone the repository with `git` (if you don't know what this means,
      keep going).
    
   4. Open a command window.
  
   5. Go to the folder where you downloaded and expanded the repository (use
      the ``cd`` command for that). There should be a file called ``conf.py`` in
      that folder.
       
   6. Type the command `make html` in the command window
	   
   7. Open the browser and look at the file _build/html/index.html that was
      created in that same folder. You should be looking at a sample of pages
      created using the authoring toolkit. Go ahead, modify them, type again
      the `make html` command and a new version is ready.

You have created your first project with Reauthoring. You can use this
directory as the initial version of the project and start reading about
`reStructuredText <http://sphinx-doc.org/rest.html>`_ and `sphinx-doc
<http://sphinx-doc.org>`__. 

