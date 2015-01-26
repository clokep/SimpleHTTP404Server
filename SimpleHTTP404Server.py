import os
import SimpleHTTPServer


class GitHubHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    """
    Overrides the default request handler to handle GitHub custom 404 pages.
    (Pretty much a 404.html page in your root.)

    See https://help.github.com/articles/custom-404-pages

    This currently only works for erroneous pages in the root directory, but
    that's enough to test what the 404 page looks like.

    """
    def do_GET(self):
        path = self.translate_path(self.path)

        # If the path doesn't exist, fake it to be the 404 page.
        if not os.path.exists(path):
            self.path = '404.html'

        # Call the superclass methods to actually serve the page.
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


SimpleHTTPServer.test(GitHubHandler)
