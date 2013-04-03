
def run_wsgiref_proxy_server(args):
    from wsgiref import simple_server
    import wsgi_proxy
    application = wsgi_proxy.WSGIProxyApplication()
    server = simple_server.make_server(args['host'], args['port'], application)

    try:
        print 'Running proxy at http://%s:%s' % (args['host'], args['port'])
        while 1:
            server.handle_request()
    except KeyboardInterrupt:
        raise SystemExit


def run_cherrypy_proxy_server(args):
    import cherrypy
    import wsgi_proxy
    application = wsgi_proxy.WSGIProxyApplication()
    server = cherrypy.wsgiserver.CherryPyWSGIServer((args['host'], args['port']), application, server_name="wsgi_proxy")
    server.start()
    try:
        while 1:
            pass
    except KeyboardInterrupt:
        server.stop()
        raise SystemExit


def main():
    import sys
    import logging
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

    if not sys.argv:
        print 'Usage: python run_proxy host=127.0.0.1 port=8080'
        raise SystemExit

    args = {'port': 8080, 'host': '127.0.0.1'}
    sys.argv.pop(0)
    for arg in sys.argv:
        if '=' not in arg:
            print 'args must be in key=value format'
            raise SystemExit
        args.__setitem__(*arg.split('='))

    if 'server' in args and args['server'] == 'cherrypy':
        run_cherrypy_proxy_server(args)
    else:
        run_wsgiref_proxy_server(args)


if __name__ == '__main__':
    main()
