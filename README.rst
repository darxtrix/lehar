lehar
=====

|Header image|

|travis\_badge| |Code Climate| |Test Coverage| |Issue Count|

Python library to generate sparklines ▁▂▄▅▇█ in your shell based upon
relative ordering of data. ``lehar`` is a `Hindi`_ word which means
wave. ``lehar`` can be invoked via *commandline* also.

.. code:: bash

    # Find commits by authors in a git repo
    $ git shortlog -s | cut -f1 | lehar
    ▇▁▁▁▁▁▁▂▃▁▁█▁▁▂▃▅▁▁▁▂▆▁▁▁▂▁▁▁▁▂▇▁▅▆▁▁▁▄▁▁█▁▁▂▁▂▁

`Some cool usage`_

Demo
----

Installation
------------

Using ``homebrew``:

.. code:: bash

    $ brew install lehar 

Using ``pip``

::

    $ pip install lehar

gi

API
---

lehar.draw(numbers,options)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

numbers
^^^^^^^

``type`` : ``list``

options
^^^^^^^

| Only supported option is ``color``
| eg. ``color='red'``

Basic Usage
^^^^^^^^^^^

.. code:: python


    >>> import lehar

    # Strings
    >>> lehar.draw(["0","1","2","3","4"])
    '▁▂▄▆█'

    # Numbers
    >>> lehar.draw([0,1,2,3,4])
    '▁▂▄▆█'

    # Negatives
    >>> lehar.draw([1,3,-34,12,44,81,0])
    '▃▃▁▄▆█▃'

    # Missing data
    >>> lehar.draw([1,3,-34,'',12,44,'',81,0])
    '▃▃▁ ▄▆ █▃'

Adding colors
^^^^^^^^^^^^^

.. code:: python

    >>> lehar.draw(["0","1","2","3","4"],color="yellow")

    >>> lehar.draw([1,3,-34,'',12,44,'',81,0],color="cyan")

Command line
------------

.. code:: bash

    $ lehar 1 2 3 4 5

    $ lehar -c red 1 2 3 4 5

    $ echo "-c cyan 1 2 3 4 5" | lehar

    $ lehar < input

Support
-------

``lehar`` supports both ``Python2`` & ``Python3``.

Contributing Guide
------------------

-  Setup

   .. code:: bash

       $ git clone https://github.com/darxtrix/lehar
       $ cd lehar 
       $ pip install -r requirements.txt
       $ python setup.py develop
       $ lehar 

-  Tests are located at ``lehar/tests.py`` and covergae tests are
   located at ``.travis.yml``

   .. code:: bash

       $ python tests.py

-  While sending a pull request increment the version at `VERSION`_ and
   make sure the travis build passes.


License
-------
MIT © [Ankush Sharma](http://github.com/darxtrix)


.. _Hindi: https://en.wikipedia.org/wiki/Hindi
.. _Some cool usage: https://github.com/holman/spark/wiki/Wicked-Cool-Usage
.. _VERSION: https://github.com/darxtrix/lehar/blob/master/lehar/VERSION

.. |Header image| image:: docs/header.png
.. |travis\_badge| image:: https://travis-ci.org/darxtrix/lehar.svg?branch=master
.. |Code Climate| image:: https://codeclimate.com/github/darxtrix/lehar/badges/gpa.svg
   :target: https://codeclimate.com/github/darxtrix/lehar
.. |Test Coverage| image:: https://codeclimate.com/github/darxtrix/lehar/badges/coverage.svg
   :target: https://codeclimate.com/github/darxtrix/lehar/coverage
.. |Issue Count| image:: https://codeclimate.com/github/darxtrix/lehar/badges/issue_count.svg
   :target: https://codeclimate.com/github/darxtrix/lehar