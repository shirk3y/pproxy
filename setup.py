from setuptools import setup, find_packages

from wsgi_proxy.version import VERSION

desc = """WSGI proxy application"""
summ = """WSGI application for a simple HTTP 1.0 proxy."""

setup(name='wsgi-prixy',
      version=VERSION,
      description='WSGI proxy application',
      summary=summ,
      author='OSAF, Mikeal Rogers',
      author_email='mikeal.rogers@gmail.com',
      url='http://code.google.com/p/wsgi-proxy/',
      license='Apache License 2.0',
      packages=find_packages(),
      platforms=['Any'],
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Console',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: Apache Software License',
                   'Operating System :: OS Independent',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                  ]
     )
