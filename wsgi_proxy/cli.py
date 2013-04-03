""":mod:`wsgi_proxy.cli` --- :program:`wsgi-proxy` command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
import logging
import optparse
import sys

from . import WSGIProxyApplication


parser = optparse.OptionParser()
parser.add_option('-p', '--port', type='int', default=8080,
                  help='Port number [default: %default]')
parser.add_option('-H', '--host', default='127.0.0.1',
                  help='Host [default: %default]')
parser.add_option('--server', default='wsgiref',
                  help='Server implementation [default: %default]')
parser.add_option('-v', '--verbose', action='store_const',
                  dest='log_level', const=logging.DEBUG,
                  help='Print debug logs as well')
parser.add_option('-q', '--quiet', action='store_const',
                  dest='log_level', const=logging.ERROR, default=logging.INFO,
                  help='Operate quietly')


def run_wsgiref_proxy_server(app, host, port):
    from wsgiref.simple_server import make_server
    server = make_server(host, port, app)
    logger = logging.getLogger(__name__ + '.run_wsgiref_proxy_server')
    logger.info('Running proxy at http://%s:%s', host, port)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        raise SystemExit


def run_cherrypy_proxy_server(app, host, port):
    from cherrypy.wsgiserver import CherryPyWSGIServer
    server = CherryPyWSGIServer((host, port), app,
                                server_name='wsgi_proxy')
    server.start()
    try:
        while 1:
            pass
    except KeyboardInterrupt:
        server.stop()
        raise SystemExit


def main():
    options, args = parser.parse_args()
    logger = logging.getLogger()
    logger.addHandler(logging.StreamHandler(sys.stdout))
    logger.setLevel(options.log_level)
    try:
        serve = globals()['run_{0}_proxy_server'.format(options.server)]
    except KeyError:
        parser.error(options.server +
                     ' is not a supported server implementation')
    app = WSGIProxyApplication()
    serve(app=app, host=options.host, port=options.port)


if __name__ == '__main__':
    main()
