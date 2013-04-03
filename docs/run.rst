Running
=======

:program:`wsgi-proxy` command
-----------------------------

The package also installs :program:`wsgi-proxy` command on your system.
It runs a proxy server on your system.

.. sourcecode:: console

   $ wsgi-proxy -p 8080

You can change the server implementation using :option:`--server
<wsgi-proxy --server>` option.
Default is ``waitress``.

.. sourcecode:: console

   $ wsgi-proxy --server wsgiref
   $ wsgi-proxy --server cherrypy


WSGI application
----------------

The package provides a WSGI app that implements HTTP proxy as its name says.
You can serve the application using any WSGI servers like `Green Unicorn`_
or Tornado_.  The application endpoint is:

:data:`wsgi_proxy.app` (or some servers accept ``wsgi_proxy:app``).

The following list shows some examples:

`Green Unicorn`_
   .. sourcecode:: console

      $ pip install gunicorn
      $ gunicorn wsgi_proxy:app

Tornado_
   .. sourcecode:: console

      $ pip install tornado

   .. sourcecode:: python

      from tornado.httpserver import HTTPServer
      from tornado.ioloop import IOLoop
      from tornado.wsgi import WSGIContainer
      from wsgi_proxy import app

      container = WSGIContainer(app)
      http_server = HTTPServer(container)
      http_server.listen(8080)
      IOLoop.instance().start()

.. seealso::

   `Servers which support WSGI`__ --- WSGI.org
      An alphabetic list of WSGI servers.

.. _Green Unicorn: http://gunicorn.org/
.. _Tornado: http://www.tornadoweb.org/
__ http://www.wsgi.org/en/latest/servers.html
