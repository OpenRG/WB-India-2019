# World Bank - Tax Policy Research Unit, 2019

This repository contains the training materials, tutorials, lecture notes, code, and problem sets for the World Bank sponsored training of TPRU staff in Delhi, India August 5-9 and August 19-23. The training will be lead by Dr. Richard W. Evans, Associate Director and Senior Lecturer at the University of Chicago M.A. Program in Computational Social Science and Dr. Jason DeBacker, Associate Professor in the Department of Economics at the University of South Carolina.

This `README.md` serves as a reference for the TPRU training. This document has seven sections.

1. [Training schedule](#1-training-schedule)
2. [Instructions for installing the Anaconda distribution of Python](#2-instructions-for-installing-the-anaconda-distribution-of-python)
3. [Text editor suggestions](#3-text-editor-suggestions)
4. [PEP 8, docstring commenting, and module structure](#4-pep-8-docstring-commenting-and-module-structure)
5. [Git and GitHub.com tutorial](#5-git-and-gitHub-tutorial)
6. [Jupyter notebooks](#6-jupyter-notebooks)
7. [Python tutorials](#7-python-tutorials)


## 1. Training Schedule

There will be two weeks of training in this program.  The first week will be held remotely via WebEx or Zoom and begins on Monday, August 5 and ends on Friday, August 9.  There will be two 2-hour sections held on Monday (August 5), Wednesday (August 7), and Friday (August 9).  The sessions will be held at 10:00am-12:00pm and 4:00pm-6:00pm, Delhi time.

The second part of the training will be held on site in Dehli from August 19-23.  During this week, participants will work 9:00am-12:00pm and 1:00pm-4:00pm.

Below is a summary schedule of topics.

### Week 1

| Meeting | Day | Date | Topics |
|:---:|:---:|:--- |:--- |
1  | M   | Aug. 5 | Git and GitHub basic, intro to Python, IDE’s and Python workflows, data types, input/output |
2  | M   | Aug. 5 | Numpy, broadcasting, indexing, pandas, visualization |
3  | W   | Aug. 7 | Object oriented programming, functions, docstrings |
4  | W   | Aug. 7 | Optimization (unconstrained, constrained) |
5  | F   | Aug. 9 | Three period lived agent OG model - theory |
6  | F   | Aug. 9 | Three period lived agent OG model - computation |

### Week 2

| Meeting | Day | Date | Topics |
|:---:|:---:|:--- |:--- |
1  | M   | Aug. 19 | Theory and components/modules of [OG-USA](https://github.com/PSLmodels/OG-USA), Downloading the model, installing packages, setting a policy |
2  | T   | Aug. 20 | Estimation of tax functions from India microsimulation model, Calibrating lifetime earnings profiles |
3  | W   | Aug. 21 | Calibrating demographics, Calibrating bequests and transfers |
4  | Th   | Aug. 22 | Calibrating labor supply and wealth distribution: chi_n^s, chi_b^j, Calibrating open economy, government closure rule |
5  | F   | Aug. 23 | Ways to run the model, how to change the model, questions/exercises |


We have provided 6 areas of tutorials that you will benefit from reading and working through before the training. We will, of course, teach these things as we go through the material. But we will be able to proceed at a faster pace if the attendees are already familiar with most of the concepts below.


## 2. Instructions for installing the Anaconda distribution of Python

We will be using the [Python](https://www.python.org/) programming language and many of its powerful libraries for writing the code that will run most of the computational methods we will use during the Boot Camp. Using an open source language, such as Python, has the advantage of being free and accessible for anyone who wishes to learn these materials or contribute to these projects. Being open source also allows Python users to go into the source code of any function to modify it to suit one's needs.

We recommend that each participant download the Anaconda distribution of Python provided by [Anaconda, Inc.](https://www.anaconda.com/distribution/) We recommend the most recent stable version of Python, which is currently Python 3.7. This can be done from the [Anaconda download page](https://www.anaconda.com/distribution/) for Windows, Mac OSX, and Linux machines.


## 3. Text editor suggestions

In our recommended Python development workflow, you will write Python scripts and modules (`*.py` files) in a text editor. Then you will run those scripts from your terminal. You will want a capable text editor for developing your code. Many capable text editors exist, but we recommend two here.

1. [Visual Studio Code](https://code.visualstudio.com)
2. [Atom](https://atom.io)


Both Visual Studio (VS) Code and Atom are completely free. In the following subsections, we provide some of the details about these text editors.

### 3.1. VS Code

VS Code will be included with your installation of Anaconda.  This is a very capable text editor and will include syntax highlighting for Python and and built in Git controls.  In addition to the basics, you may want to use a more advanced linter for Python.  This will help you correct syntax errors on the fly and provide helpful information as you declare objects and call functions.  [This link](https://code.visualstudio.com/docs/python/linting) provides step-by-step instructions on using more advanced linting in VS Code.

### 3.2. Atom

[Atom](https://atom.io) is an open source text editor developed by people at GitHub.com. This editor has all the features of Sublime Text 3, but it also allows users full customizability. Further, it has been a while now that the users of Atom have surpassed the critical mass necessary to keep the editor progressing with the most cutting edge additions.

There are several packages you'll want to install with Atom.  Once Atom is installed, you can add packages by navigating Atom->Preferences->Install and then typing in the name of the package you would like to install.

For work with Python, we recommend the following packages be installed:

* MagicPython
* python-indent
* tabs-to-spaces
* minimap
* open-recent
* linter-python-pep8

For development with GitHub we recommend:

* merge-conflict


## 4. PEP 8, docstring commenting, and module structure

Computer code executes some set of commands in an organized way. In every case, there are often many ways to execute a set of instructions--some ways more efficient than others. However, code has at least three functions.

1. Efficiently execute the task at hand.
2. Be accessible and usable to other programmers.
3. Be scalable and integrable with other projects and procedures.

Bill Gates is credited with the following plea for efficiency and parsimony in code writing.

> "Measuring programming progress by lines of code is like measuring aircraft building progress by weight."

Strong support for points (2) and (3) is Eagleson's Law.

> "Any code of your own that you haven't looked at for six or more months might as well have been written by someone else."

Because of the latter two characteristics, Python code has developed some conventions and best practices, some of which have been institutionalized in the [PEP 8--Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/) ("PEP" stands for Python Enhancement Proposals). Key examples PEP 8 Python coding conventions are the following.

* Indents should be 4 spaces (not tab)
* Limit all lines to a maximum of 79 characters long blocks of text being limited to 72 characters (Evans limits all his lines to 72 characters)
* Use a space after a comma
* Use a space before and after arithmetic operators

In the text editors Atom, Sublime Text 3, and Vim, you can install Linter packages that highlight areas of your code that break PEP 8 rules and tell you what the violation is.

There are fewer conventions in docstring structure, but we have developed some of our own that are outlined in the [PythonFuncs.ipynb](https://github.com/OpenSourceMacro/BootCamp2019/blob/master/Tutorials/PythonFuncs.ipynb) Jupyter notebook. See especially Sections 3 and 4 of the Jupyter notebook.


## 5. Git and GitHub tutorial

We have included a tutorial on using [Git and GitHub.com](https://github.com/OpenSourceMacro/BootCamp2019/blob/master/Tutorials/git_tutorial.pdf) in the [Tutorials](https://github.com/OpenSourceMacro/BootCamp2019/tree/master/Tutorials) directory of this repository. Git is a powerful version control software that comes natively installed on many machines and is widely used. GitHub.com is the most widely used online platform for hosting open source projects and integrating with Git software. Git has a significant learning curve, but it is essential for large collaborations that involve software development.

A more comprehensive Git resource is [*Pro Git*](https://git-scm.com/book/en/v2), by Chacon and Straub (2014). This book is open access, and is available online at [https://git-scm.com/book/en/v2](https://git-scm.com/book/en/v2). But Evans likes having it in his library in hard copy. This book is the difinitive guide with everything Git, and it has as its primary application the interaction between Git and GitHub. However, the workflow described in the tutorial above was hard to find in this Git book.


## 6. Jupyter Notebooks

[Jupyter notebooks](http://jupyter.org/) are files that end with the `*.ipynb` suffix. These notebooks are opened in a browser environment and are an open source web application that combines instructional text with live executable and modifyable code for many different programming platforms (e.g., Python, R, Julia). Jupyter notebooks are an ideal tool for teaching programming as they provide the code for a user to execute and they also provide the context and explanation for the code. We have provided a number of Jupyter notebooks in the [Tutorials](https://github.com/OpenSourceMacro/BootCamp2019/tree/master/Tutorials) folder of this repository.

These notebooks used to be Python-specific, and were therefore called iPython notebooks (hence the `*.ipynb` suffix). But Jupyter notebooks now support many programming languages, although the name still pays homage to Python with the vestigal "py" in "Jupyter". The notebooks execute code from the kernel of the specific programming language on your local machine.

Jupyter notebooks capability will be automatically installed with your download of the [Anaconda distribution](https://www.anaconda.com/download/) of Python. If you did not download the Anaconda distribution of Python, you can download Jupyter notebooks separately by following the instructions on the Jupyter [install page](http://jupyter.org/install).


### 6.1. Opening a Jupyter notebook

Once Jupyter is installed--whether through Anaconda or through the Jupyter website--you can open a Jupyter notebook by the following steps.

1. Navigate in your terminal to the folder in which the Jupyter notebook files reside. In the case of the Jupyter notebook tutorials in this repository, you would navigate to the `~/BootCamp2019/Tutorials/` directory.
2. Type `jupyter notebook` at the terminal prompt.
3. A Jupyter notebook session will open in your browser, showing the available `*.ipynb` files in that directory.
  *  In some cases, you might receive a prompt in the terminal telling you to paste a url into your browser.
4. Double click on the Jupyter notebook you would like to open.

It is worth noting that you can also simply navigate to the URL of the Jupyter notebook file in the GitHub repository on the web (e.g., [https://github.com/OpenSourceMacro/BootCamp2019/blob/master/Tutorials/PythonReadIn.ipynb](https://github.com/OpenSourceMacro/BootCamp2019/blob/master/Tutorials/PythonReadIn.ipynb)). You can read the Jupyter notebook on GitHub.com, but you cannot execute any of the cells. You can only execute the cells in the Jupyter notebook when you follow the steps above and open the file from a Jupyter notebook session in your browser.


### 6.2. Using an open Jupyter notebook

Once you have opened a Jupyter notebook, you will find the notebook has two main types of cells: Markdown cells and Code cells. Markdown cells have formatted Jupyter notebook markdown text, and serve primarily to present context for the coding cells. A reference for the markdown options in Jupyter notebooks is found in the [Jupyter markdown documentation page](http://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/Working%20With%20Markdown%20Cells.html).

You can edit a Markdown cell in a Jupyter notebook by double clicking on the cell and then making your changes. Make sure the cell-type box in the middle of the top menu bar is set to `Markdown`. To implement your changes in the Markdown cell, type `Shift-Enter`.

A Code cell will have a `In [ ]:` immediately to the left of the cell for input. The code in that cell can be executed by typing `Shift-Enter`. For a Code cell, the  cell-type box in the middle of the top menu bar says `Code`.


### 6.3. Closing a Jupyter notebook

When you are done with a Jupyter notebook, you first save any changes that you want to remain with the notebook. Then you close the browser windows associated with that Jupyter notebook session. You should then close the local server instance that was opened to run the Jupyter notebook in your terminal window. On a Mac or Windows, this is done by going to your terminal window and typing `Cmd-C` or `Ctrl-C` and then selecting `y` for yes and hitting `Enter`.


## 7. Python tutorials

For this training, we have included in this repository six basic Python tutorials in the [`Tutorials`](https://github.com/OpenRG/WB-India-2019/tree/master/Tutorials) directory.

1. [PythonReadIn.ipynb](https://github.com/OpenRG/WB-India-2019/tree/master/Tutorials/PythonReadIn.ipynb). This Jupyter notebook provides instruction on basic Python I/O, reading data into Python, and saving data to disk.
2. [PythonNumpyPandas.ipynb](https://github.com/OpenRG/WB-India-2019/tree/master/Tutorials/PythonNumpyPandas.ipynb). This Jupyter notebook provides instruction on working with data using `NumPy` as well as Python's powerful data library `pandas`.
3. [PythonDescribe.ipynb](https://github.com/OpenRG/WB-India-2019/tree/master/Tutorials/PythonDescribe.ipynb). This Jupyter notebook provides instruction on describing, slicing, and manipulating data in Python.
4. [PythonFuncs.ipynb](https://github.com/OpenRG/WB-India-2019/tree/master/Tutorials/PythonFuncs.ipynb). This Jupyter notebook provides instruction on working with and writing Python functions.
5. [PythonVisualize.ipynb](https://github.com/OpenRG/WB-India-2019/tree/master/Tutorials/PythonVisualize.ipynb). This Jupyter notebook provides instruction on creating visualizations in Python.
6. [PythonRootMin.ipynb](https://github.com/OpenRG/WB-India-2019/tree/master/Tutorials/PythonRootMin.ipynb). This Jupyter notebook provides instruction on implementing univariate and multivariate root finders and unconstrained and constrained minimizers using functions in the [`scipy.optimize`](https://docs.scipy.org/doc/scipy/reference/optimize.html) sub-library.

To further one's Python programming skills, a number of other great resources exist.

* The [official Python 3 tutorial site](https://docs.python.org/3/tutorial/)
* [QuantEcon.net](https://lectures.quantecon.org/py/) is a site run by [Thomas Sargent](http://www.tomsargent.com/) (NYU Stern) and [John Stachurski](http://johnstachurski.net/) (Australia National University). QuantEcon has a very large number of high-quality economics focused computational tutorials in Python. The first three sections provide a good introduction to Python programming.
* [Python computational labs](http://www.acme.byu.edu/2017-2018-materials/) of the Applied and Computational Mathematics Emphasis at Brigham Young University.
* [Code Academy's Python learning module](https://www.codecademy.com/learn/learn-python)
