""":mod:`wsgi_proxy` --- WSGI proxy app
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
import copy
import httplib
import logging
import urlparse

logger = logging.getLogger(__name__)

_hoppish = {
    'connection': 1, 'keep-alive': 1, 'proxy-authenticate': 1,
    'proxy-authorization': 1, 'te': 1, 'trailers': 1, 'transfer-encoding': 1,
    'upgrade': 1, 'proxy-connection': 1 }


def is_hop_by_hop(header):
    return _hoppish.has_key(header.lower())


def reconstruct_url(environ):
    # From WSGI spec, PEP 333
    url = environ.get('PATH_INFO', '')
    # Fix ;arg=value in url
    if url.find('%3B') is not -1:
        url, arg = url.split('%3B', 1)
        url = ';'.join([url, arg.replace('%3D', '=')])
    # Stick query string back in
    if environ.get('QUERY_STRING'):
        url += '?' + environ['QUERY_STRING']
    environ['reconstructed_url'] = url
    return url


class WSGIProxyApplication(object):
    """Application to handle requests that need to be proxied"""

    ConnectionClass = httplib.HTTPConnection

    def handler(self, environ, start_response):
        """Proxy for requests to the actual http server"""
        url = urlparse.urlparse(reconstruct_url(environ))

        # Create connection object
        try:
            connection = self.ConnectionClass(url.netloc)
            # Build path
            path = url.geturl().replace('%s://%s' % (url.scheme, url.netloc),
                                        '')
        except Exception:
            start_response("501 Gateway error", [('Content-Type', 'text/html')])
            logger.exception('Could not Connect')
            return ['<H1>Could not connect</H1>']

        # Read in request body if it exists
        body = None
        if environ.get('CONTENT_LENGTH'):
            length = int(environ['CONTENT_LENGTH'])
            body = environ['wsgi.input'].read(length)

        # Build headers
        headers = {}
        logger.debug('Environ ; %s' % str(environ))
        for key in environ.keys():
            # Keys that start with HTTP_ are all headers
            if key.startswith('HTTP_'):
                # This is a hacky way of getting the header names right
                value = environ[key]
                key = key.replace('HTTP_', '', 1).swapcase().replace('_', '-')
                if is_hop_by_hop(key) is False:
                    headers[key] = value

        # Handler headers that aren't HTTP_ in environ
        if environ.get('CONTENT_TYPE'):
            headers['content-type'] = environ['CONTENT_TYPE']

        # Add our host if one isn't defined
        if not headers.has_key('host'):
            headers['host'] = environ['SERVER_NAME']

        # Make the remote request
        try:
            logger.debug(
                '%s %s %s' %
                (environ['REQUEST_METHOD'], path, str(headers))
            )
            connection.request(environ['REQUEST_METHOD'], path,
                               body=body, headers=headers)
        except:
            # We need extra exception handling in the case the server fails
            # in mid connection, it's an edge case but I've seen it
            start_response("501 Gateway error", [('Content-Type', 'text/html')])
            logger.exception('Could not Connect')
            return ['<H1>Could not connect</H1>']

        response = connection.getresponse()

        hopped_headers = response.getheaders()
        headers = copy.copy(hopped_headers)
        for header in hopped_headers:
            if is_hop_by_hop(header[0]):
                headers.remove(header)

        start_response(response.status.__str__() + ' ' + response.reason,
                       headers)
        return [response.read(response.length)]

    def __call__(self, environ, start_response):
        return self.handler(environ, start_response)
