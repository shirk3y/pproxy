Installtion
===========

The latest release
------------------

The easiest way to install :program:`wsgi-proxy` is to use :program:`pip` or
:program:`easy_install`:

.. sourcecode:: console

   $ pip install wsgi-proxy


Bleeding edge
-------------

You can install it from the repository if you use :program:`pip`:

.. sourcecode:: console

   $ pip install hg+https://bitbucket.org/dahlia/wsgi-proxy


For contribution
----------------

If you want to contribute to the project, you should clone the repository first.
We use Mercurial_.

.. sourcecode:: console

   $ hg clone https://bitbucket.org/dahlia/wsgi-proxy

:program:`pip` can install the package as editable mode through ``-e`` option.
It just makes a link to the working directory in :file:`site-packages`.

.. sourcecode:: console

   $ cd wsgi-proxy/
   $ pip install -e .

Or you can use ``develop`` command :file:`setup.py` script provides:

.. sourcecode:: console

   $ cd wsgi-proxy/
   $ python setup.py develop

.. _Mercurial: http://mercurial.selenic.com/
