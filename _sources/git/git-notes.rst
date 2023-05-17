Git temporal notes
==================

.. contents::
    :depth: 1
    :local:
    :backlinks: entry

Update token to connect to remote repository
--------------------------------------------

1. git remote remove origin
2. git remote add origin https://<token>@github.com/<user>/<repo>.git
3. git push --set-upstream origin main
