*******************************************************************************
Nuevo Libro
*******************************************************************************
    
.. contents::
    :depth: 1
    :local:
    :backlinks: entry

Cada libro (o carpeta), cuenta 2 archivos: *index.rst* y *chapter_x.rst*. El primero es la información que aparece el
ingresar al libro (puede ser una especie de introducción), y el segundo es un capítulo del libro, el nombre del archivo
puede ser cualquiera.

El siguiente script crea la carpeta y archivos necesarios para iniciar un libro.

.. code-block:: console
   :caption: Habre la terminal en la carpeta "docs" de la biblioteca (Ej. the_beavers_hut). 

   source/user_guide/add_book.sh


Descripción de los archiovs .rst:

.. code-block:: rst
   :caption: Libro (introducción).

   ###############################################################################
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

      *


.. code-block:: rst
   :caption: Capítulo.

   *******************************************************************************
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
   """""""""""""""""""





