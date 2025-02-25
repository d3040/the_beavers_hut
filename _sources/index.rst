################################################################################
The Beaver's Hut
################################################################################
   
.. toctree::
   :hidden:
   :caption: Libros
   :maxdepth: 1
   :glob:

   */index


*******************************************************************************
Intro
******************************************************************************* 

|

  If you work for 10 years, do you get 10 years of experience or
  do you get 1 year of experience 10 times? You have to reflect on
  your activities to get true experience. If you make learning a
  continuous commitment, you’ll get experience. If you don’t, you won’t,
  no matter how many years you have under your belt.

  -- Steve McConnell, Software Engineer.

|

* Always have a project. Then learn what you need to learn en route to finishing that project.
* Together, we face the fundamental problems of our time:
  
  - Access to information,
  - Access to education, and 
  - Access to the tools that are shaping the future.


* There are three big reasons why learning to code is so hard, even today:
  
  - The tools are still primitive.
  - Most people aren't good at handling ambiguity, and learning to code is ambiguous. People get lost.
  - Most people aren't good at handling constant negative feedback. And **learning to code is one brutal error message after another**. People get frustrated.
  - How Not to Get Frustrated: The key, again, is practice.


* People think software development is about typing code into a computer. But it's really about learning.
* Get comfortable with ambiguity and you will go far.
* Tip #1: Know that you are not uniquely bad at this.
* Tip #2: Breathe.
* Tip #3: Use Rubber Duck Debugging (Rubber Duck Debugging is a method of debugging code by explaining it out loud, often to an inanimate object like a rubber duck).
* Well, here's a theory: what you learn in university is less important than whether you finished university. Employers are trying to select for people who can figure out a way to get through this rite of passage.

|

  Computer science education cannot make anybody an expert programmer 
  any more than studying brushes and pigment can make somebody an expert painter.

  -- Eric Raymond, Developer, Computer Scientist, and Author.

|

`How to Learn to Code and Get a Developer Job <https://www.freecodecamp.org/news/learn-to-code-book/>`_

*******************************************************************************
Objetivo
*******************************************************************************

1. Salir del *tutorial hell* [#]_
2. Notas siempre al alcance.

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

   source/user_guide/add_book.sh


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

|

  If you want to go fast, go alone. 
  If you want to go far, go together.

  -- African Proverb

|

.. [#] Tutorial hell is where you jump from one tutorial to the next, learning and then relearning the same basic things. But never really going beyond the fundamentals.
.. [#] `Section Structure (rst Cheatsheet) <https://bashtage.github.io/sphinx-material/rst-cheatsheet/rst-cheatsheet.html>`_

