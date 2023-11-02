*****************
Vi IMproved (Vim)
*****************
    
.. contents::
    :depth: 1
    :local:
    :backlinks: entry

.. toctree::
    :maxdepth: 1
    :glob:

    *

* `Beginner´s guide <https://www.openvim.com/tutorial.html>`_
* `Vim adventures <https://vim-adventures.com/>`_
* `VIM and Python <https://realpython.com/vim-and-python-a-match-made-in-heaven/>`_
  
###########
Cheat Sheet
###########

.. hlist::
    :columns: 3

    * :kbd:`esc`: normal mode.
    * :kbd:`i` | :kbd:`I`: insert mode. 
    * :kbd:`v`: visual mode.
    * :kbd:`h`: move left through the text in insert mode.
    * :kbd:`j`: move down through the text in insert mode.
    * :kbd:`k`: move up through the text in insert mode.
    * :kbd:`l`: move right through the text in insert mode.
    * :kbd:`w`: moves to the start of next word.
    * :kbd:`e`: moves to the end of the next word.
    * :kbd:`b`: moves to the beginning of the previous word.
    * :kbd:`g` + :kbd:`e`: moves to the end of the previous word.
    * [n] + [action / movement]: do n times the selected action or move. 
    * [n] + :kbd:`i` + [word] + :kbd:`esc`: write n times the word.
    * :kbd:`x` | :kbd:`X`: remove character.
    * :kbd:`a` | :kbd:`A`: append.
    * :kbd:`f` + [char]: move to next given char in line.
    * :kbd:`F` + [char]: move to previous given char in line.
    * :kbd:`;` | :kbd:`,`: repeat last f or F.
    * :kbd:`/` + [word] + :kbd:`n` | :kbd:`N`: search next word.
    * :kbd:`d` + [movement]: delete by giving movement.
    * :kbd:`D`: delete to the end of line.
    * :kbd:`r` + [char]: replaces character below cursos.
    * :kbd:`%`: jump to the matching **)**, **]** or **}**.
    * :kbd:`0`: move to start of line.
    * :kbd:`$`: move to end of line.
    * :kbd:`o`: insert new line below current line and go to **insert** mode.
    * :kbd:`O`: insert new line above current line and go to **insert** mode.
    * :kbd:`c` + :kbd:`i` + [movement]: change inside of given movement.
    * :kbd:`S`: clear current line; to insert mode.
    * :kbd:`g` + :kbd:`g`: takes to the beginning of the file.
    * [n] + :kbd:`G`: takes to the n line of the file.
    * :kbd:`G`: takes to the end of the file.
    * :kbd:`y` + :kbd:`y`: copy current line.
    * :kbd:`p`: paste copied text after cursor.
    * :kbd:`*`: .
    * :kbd:`#`: .
    * :kbd:`.`: repeat previous command.
    * :kbd:`:` + :kbd:`w`: save.
    * :kbd:`:` + :kbd:`q`: quit.
    * :kbd:`:` + :kbd:`q` + :kbd:`!`: quit with out saving.
    * :kbd:`u`: undo.
    * :kbd:`Ctrl` + :kbd:`R`: redo.
    * :kbd:`:` + :kbd:`help`: when having a problem, or want to learn more about what Vim offers.



Hacks
=====

* Find and Replace: ``:[range]s/{pattern}/{string}/[flags]``
  
  + [range]: pass a range of lines. Pass % to find and replace in all lines. Use two numbers separated by a comma to indicate range (eg. 5,10), use a *dot* . to represent the current line and *$* for the las line of the file.
  + {pattern}: pass regex patterns here.
  + {string}: replacement string.
  + [flags]: additional flags, for example: *c* to confirm before replacement, *i* to change to case-insensitive search, and *g* make a change globally.  

