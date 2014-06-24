Changelog
=========

Version 0.3.1
-------------

To be released.

- Fix a url reconsturction bug on several WSGI servers like `Green Unicorn`_.
  Now it sees ``HTTP_HOST`` and ``wsgi.url_scheme`` when ``PATH_INFO`` is
  not enough.  [:issue:`1`]

.. _Green Unicorn: http://gunicorn.org/


Version 0.3.0
-------------

Released on April 5, 2013.  It's a first version released by `Hong Minhee`__,
a new maintainer of :program:`wsgi-proxy`.

- Introduce new :program:`wsgi-proxy` command.
- Use waitress_ by default.
- Add :data:`wsgi_proxy.app`, a default instance of
  :class:`wsgi_proxy.WSGIProxyApplication`.
- Fix :func:`~wsgi_proxy.reconstruct_url()` to correctly constructs
  the remote URL.  [`#1 from Google Code`__]

__ http://hongminhee.org/
__ http://code.google.com/p/wsgi-proxy/issues/detail?id=1
.. _waitress: https://github.com/Pylons/waitress
