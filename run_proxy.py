#!/usr/bin/env python
# -- Example server run

def run_wsgiref_proxy_server():
    from wsgiref import simple_server
    import wsgi_proxy
    application = wsgi_proxy.WSGIProxyApplication()
    server = simple_server.make_server(args['host'], args['port'], application)

    try:
        print 'Running proxy at http://%s:%s' % (args['host'], args['port'])
        while 1:
            server.handle_request()
    except KeyboardInterrupt:
        sys.exit()
        
def run_cherrypy_proxy_server():
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
        sys.exit()
    

if __name__ == "__main__":
    import sys
    import logging
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    
    if len(sys.argv) is 1:
        print 'Usage: python run_proxy host=127.0.0.1 port=8080'
        sys.exit
    
    args = {'port':8080, 'host':'127.0.0.1'}
    sys.argv.pop(0)
    for arg in sys.argv:
        if arg.find('=') is -1:
            print 'args must be in key=value format'
            sys.exit()
        args.__setitem__(*arg.split('='))
    
    if args.has_key('server') and args['server'] == 'cherrypy':
        run_cherrypy_proxy_server()
    else:
        run_wsgiref_proxy_server()
    
        
    
