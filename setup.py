import os
from setuptools import setup


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()


setup(
    name='SimpleHTTP404Server',
    version='0.2.0',
    description='A Python SimpleHTTPServer, but serves 404.html if a page is not found.',
    long_description=(read('README.rst') + '\r\n' +
                      read('CHANGELOG.rst') + '\r\n'),
    url='http://github.com/clokep/SimpleHTTP404Server/',
    license='MIT',
    author='Patrick Cloke',
    author_email='patrick@cloke.us',
    py_modules=['SimpleHTTP404Server'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
