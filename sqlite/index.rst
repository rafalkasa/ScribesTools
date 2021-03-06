.. _`SQLite chapter`:

SQLite
======

SQLite_ is a file-based SQL database system.

.. _`SQLite Installation`:

Installation
------------

*   download the "command line shell” for "sqlite3" from
    `SQLite download page`_.
    For Windows download ``sqlite-shell-win32-x86-3081002.zip``
    |SQLiteWin32zip|.
*   create a directory where you want to install sqlite3 (e.g.
    ``%SCRIBESTOOLS%\SQLite``)
*   extract the archive (only one file on windows: ``sqlite3.exe``)
*   move the content of the archive to the directory created
*   add ``%SCRIBESTOOLS%\SQLite`` to the path.

On Ubuntu you can install SQLite_ as following::

    sudo apt-get install sqlite3

Launching SQLite
----------------

You can test the installation and check the version of sqlite3 with the
following command::

    sqlite3 -version

Then try::

    sqlite3

This should launch the SQLite_ shell. Try the following commands::

    .help
    .schema
    .quit

Since no database has been specified when launching the shell command the
``.schema`` command will not display anything.


Sqlite3 for django
------------------
If you use SQLite_ with django, then you can launch the shell with the
following commands::

    python manage.py dbshell


Documentation
-------------
The documentation is available online (`SQLite documentation`_).

* `SQLite dialect`_.
* SQL features `omitted from SQLite`_

To get some help about the command line type::

    sqlite3 -help

If you want some brief help about the shell commands (including SQL) you can
type in the shell::

    .help

More generally, the documentation of the shell is available at
https://www.sqlite.org/cli.html



.. .....................................................................

..  _SQLite:
    https://www.sqlite.org/

..  _`SQLite download page`:
    https://www.sqlite.org/download.html

..  _`SQLite documentation`:
    https://www.sqlite.org/docs.html

..  |SQLiteWin32zip| replace::
    `web <https://www.sqlite.org/2015/sqlite-shell-win32-x86-3081002.zip>`__

..  |SQLiteJDBCJar| replace::
    `web <https://bitbucket.org/xerial/sqlite-jdbc/downloads/sqlite-jdbc-3.8.10.1.jar>`__

..  _`SQLite dialect`:
    https://www.sqlite.org/lang.html

..  _`omitted from SQLite`:
    https://www.sqlite.org/omitted.html