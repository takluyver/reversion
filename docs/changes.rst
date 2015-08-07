Specifying version number changes
=================================

At the command line, you can specify a few ways to change the version number:

* Starts with a number - set a completely new version number::

      reversion 4.0

* Starts with ``~`` - add a suffix to the current version::

      reversion ~.1
      # 4.0 -> 4.0.1

* Starts with ``+`` - increment the current version::

      reversion +.1
      # 4.0 -> 4.1

  Any non-numeric parts have to match exactly, so you can do::

      reversion +..0beta1
      # 4.0.0beta1 -> 4.0.0beta2

* The word ``final`` - strip any non-numeric version parts::

      reversion final
      # 4.0.0rc3 -> 4.0.0

You can also chain changes together. For instance, immediately after a major
release, you may want to increment the version number and add a dev suffix::

    reversion +1 ~.dev0
    # 4.0.0 -> 5.0.0.dev0

