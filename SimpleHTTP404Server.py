import os
import SimpleHTTPServer


class GitHubHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    """
    Overrides the default request handler to handle GitHub custom 404 pages.
    (I.e. a 404.html page located in the root.)

    See https://help.github.com/articles/custom-404-pages

    """
    def do_GET(self):
        path = self.translate_path(self.path)

        # If the path doesn't exist, fake it to be the 404 page.
        if not os.path.exists(path):
            path = '404.html'
            # This is based on ``send_head`` of ``SimpleHTTPRequestHandler``.
            ctype = self.guess_type(path)
            try:
                # Always read in binary mode. Opening files in text mode may cause
                # newline translations, making the actual size of the content
                # transmitted *less* than the content-length!
                f = open(path, 'rb')

                try:
                    # Ensure we return a 404.
                    self.send_response(404)
                    self.send_header("Content-type", ctype)
                    fs = os.fstat(f.fileno())
                    self.send_header("Content-Length", str(fs[6]))
                    self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
                    self.end_headers()

                    # Send the actual content.
                    self.copyfile(f, self.wfile)

                    # Stop processing.
                    return
                except:
                    f.close()
                    raise
            except IOError:
                # 404.html doesn't exist, default back to the superclass.
                pass

        # Call the superclass methods to actually serve the page.
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


if __name__ == '__main__':
    SimpleHTTPServer.test(GitHubHandler)
