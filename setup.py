from setuptools import setup, find_packages

from wsgi_proxy.version import VERSION


setup(
    name='wsgi-prixy',
    version=VERSION,
    description='WSGI proxy application',
    author='OSAF, Mikeal Rogers',
    author_email='mikeal.rogers' '@' 'gmail.com',
    maintainer='Hong Minhee',
    maintainer_email='minhee' '@' 'dahlia.kr',
    url='http://code.google.com/p/wsgi-proxy/',
    license='Apache License 2.0',
    packages=find_packages(),
    platforms=['Any'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
