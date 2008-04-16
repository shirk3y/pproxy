#   Copyright (c) 2006-2007 Open Source Applications Foundation
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from setuptools import setup, find_packages

desc = """WSGI proxy application"""
summ = """WSGI application for a simple HTTP 1.0 proxy."""

PACKAGE_NAME = "wsgi-proxy"
PACKAGE_VERSION = "0.2.6pre"

setup(name=PACKAGE_NAME,
      version=PACKAGE_VERSION,
      description=desc,
      summary=summ,
      author='OSAF, Mikeal Rogers',
      author_email='mikeal.rogers@gmail.com',
      url='http://code.google.com/p/wsgi-proxy/',
      license='http://www.apache.org/licenses/LICENSE-2.0',
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
