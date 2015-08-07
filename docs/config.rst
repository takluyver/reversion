The config file
===============

The config file should be called ``reversion.toml``, and be in the root
directory of your project. ``reversion`` will look in the current directory
when you invoke it.

The config file uses the `TOML format <https://github.com/toml-lang/toml#toml>`__.

Here's reversion's own config file:

.. literalinclude:: ../reversion.toml
   :language: cfg

.. describe:: currentversion

   The current version number of the project. This is used to find the version
   number in files. Reversion will automatically update it along with the other
   version numbers.

Place sections
--------------

Each instance of the version number in your code should have a corresponding
``[[place]]`` section.

.. describe:: file

   The file containing the version number. Paths are relative to the directory
   containing ``reversion.toml``.

.. describe:: line-regex

   A regular expression to find the line with the version number. Reversion will
   only see lines matching both this pattern and the current version number.
   You probably want to specify this using a single-quoted string - this is a
   literal string in TOML syntax, so you don't need to escape backslashes.
