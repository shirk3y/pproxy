Changelog
=========

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

__ http://dahlia.kr/
__ http://code.google.com/p/wsgi-proxy/issues/detail?id=1
.. _waitress: https://github.com/Pylons/waitress
