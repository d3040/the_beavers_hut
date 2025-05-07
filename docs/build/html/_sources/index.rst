################################################################################
The Beaver's Hut
################################################################################
   
.. toctree::
   :hidden:
   :caption: Libros
   :maxdepth: 2
   :glob:

   */index
   link-lodge

*******************************************************************************
Objetivo
*******************************************************************************

1. Notas siempre al alcance.

*******************************************************************************
Manual de usuario
*******************************************************************************

Utiliza este formato para crear tus libros. Los títulos van subrayados (o sobre y subrayados) con un símbolo no alfanumérico al menos el largo del texto. 

Por sí sola, la sección con nivel superior se utiliza como el título del documento.

Cualquier símbolo alfanumérico se puede utilizar para la jerarquía de secciones.
La convención utilizada por Python es la siguiente [#]_:

* ``#``: libros (sobre y subrayado),
* ``*``: capítulos (sobre y subrayado),
* ``=``: secciones (subrayado),
* ``-``: subsecciones (subrayado),
* ``^``: subsubsecciones (subrayado), y
* ``"``: párragos (subrayado).

Nuevo Libro
===========

Cada libro (o carpeta) está compuesto por 2 archivos: *index.rst* y *chapter_x.rst*. El primero es la información que aparece el
ingresar al libro, puede usarse como introducción o descripción del libro; y el segundo es un capítulo del libro.

El siguiente script crea la carpeta y archivos necesarios para inicializar un libro.

.. code-block:: console
   :caption: Corre este script dentro de la carpeta docs de la biblioteca. 

   source/add_book.sh


Descripción de los archivos .rst:

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
      :caption: TOC's title
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

.. [#] `Section Structure (rst Cheatsheet) <https://bashtage.github.io/sphinx-material/rst-cheatsheet/rst-cheatsheet.html>`_

