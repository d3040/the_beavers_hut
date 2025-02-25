#! /bin/sh

# This program creates a new book.
# The template structure:
#
# Book
# - index.rst
# - chapter.rst
#
# Each rst file comes with the basic structure.

mkdir ~/Documents/the_beavers_hut/docs/source/books_title
touch ~/Documents/the_beavers_hut/docs/source/books_title/index.rst
touch ~/Documents/the_beavers_hut/docs/source/books_title/chapter_title.rst
echo "###############################################################################
Book's Title
###############################################################################

.. contents::
   :depth: 1
   :local:
   :backlinks: entry

.. toctree::
   :caption: chapter_x
   :maxdepth: 1
   :glob:

   *" > ~/Documents/the_beavers_hut/docs/source/books_title/index.rst
echo '*******************************************************************************
Chapter
*******************************************************************************
    
.. contents::
   :depth: 1
   :local:
   :backlinks: entry

This is a Section
=================

This is a Sub-Section
---------------------

This is a Sub-Sub-Section
^^^^^^^^^^^^^^^^^^^^^^^^^

This is a Paragraph
"""""""""""""""""""' > ~/Documents/the_beavers_hut/docs/source/books_title/chapter_title.rst

