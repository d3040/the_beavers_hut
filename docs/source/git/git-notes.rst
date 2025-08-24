Git temporal notes
==================

.. contents::
    :depth: 1
    :local:
    :backlinks: entry

Update token to connect to remote repository
--------------------------------------------

.. code-block:: sh
    :linenos:

    git remote remove origin
    git remote add origin https://<token>@github.com/<user>/<repo>.git
    git push --set-upstream origin main

