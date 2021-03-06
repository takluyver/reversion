Reversion is a command line tool to easily update version numbers in project
files.

To install it::

    pip install reversion

Python 3 is required.

To use it, create a config file ``reversion.toml`` in the root directory of your
project. It should look like this::

    currentversion = "0.1"

    [[place]]
    file = "reversion/__init__.py"
    # linematch is a regex; use single quotes so you don't have to escape backslash
    line-regex = '__version__'

    [[place]]
    file = "docs/conf.py"
    line-regex = 'release'

Each ``[[place]]`` table indicates where a copy of the version number is found.

Then run::

    reversion +0.1

To check the config file and version number places without changing anything, run::

    reversion --check

