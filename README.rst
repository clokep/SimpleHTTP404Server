SimpleHTTP404Server: Easy testing of 404.html
=============================================

*SimpleHTTP404Server* allows easy testing of static HTML providers that allow
404 response customization via a 404.html page. This includes at least GitHub_
and FastMail_. It is a simple extension to SimpleHTTPServer_, a built-in Python
module which servers the current directory over HTTP.

If you server a static site using `GitHub Pages`_ or another static website
provider, this module can help you test your 404 page before pushing changes to
a live website.

First install the package using pip:

.. code-block:: bash

    pip install SimpleHTTP404Server

Browse to the directory, and run the following to server it on port 8000.

.. code-block:: bash

    python -m SimpleHTTP404Server

Or, if you'd like to specify a different port:

.. code-block:: bash

    python -m SimpleHTTP404Server 1234

And that's it! Now browse to a page that exists, maybe
http://localhost:8000/index.html. And check that your 404.html page is properly
loaded by checking a few different paths:

* http://localhost:8000/404.html
* http://localhost:8000/does-not-exist.html
* http://localhost:8000/does/not/exist.html

.. _GitHub: https://help.github.com/articles/custom-404-pages/
.. _FastMail: https://www.fastmail.com/help/files/website.html
.. _SimpleHTTPServer: https://docs.python.org/2/library/simplehttpserver.html
.. _GitHub Pages: https://help.github.com/articles/what-are-github-pages/

Usecases
========

Personally this is used to test any GitHub Pages sites I use, in particular my
blog_, which is build on Pelican_. This is done via Fabric_:

.. code-block:: python

    @task
    def serve():
        """Locally serve the blog."""
        local('cd {deploy_path} && python -m SimpleHTTP404Server {listen_port}'.format(**env))

.. _blog: http://patrick.cloke.us
.. _Pelican: http://blog.getpelican.com/
.. _Fabric: http://www.fabfile.org/

Future
======

Please let me know (by filing issues or pull requests) if you find any bugs or
if you feel there are features missing.
