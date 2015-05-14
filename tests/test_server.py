import os
import subprocess
from unittest import TestCase

import requests

class Test404Server(TestCase):
    PORT = 8000

    def setUp(self):
        # Start the server, be sure to include the proper Python files on the
        # path.
        env = os.environ.copy()
        env["PYTHONPATH"] = os.getcwd()
        self.proc = subprocess.Popen(['python', '-u', '-m', 'SimpleHTTP404Server'],
                                     stdout=subprocess.PIPE,
                                     cwd=os.path.join(os.getcwd(), 'tests'),
                                     env=env)

        # Wait for the process to start listening...
        while True:
            line = self.proc.stdout.readline()
            if line:
                break

    def tearDown(self):
        # Stop the server.
        self.proc.kill()

    def test_real_file(self):
        r = requests.get('http://localhost:%d/test.html' % self.PORT)
        self.assertEqual(r.text, "Test page!\n")

    def test_404_direct(self):
        r = requests.get('http://localhost:%d/404.html' % self.PORT)
        self.assertEqual(r.text, "404, yay!\n")

    def test_unknown_file(self):
        r = requests.get('http://localhost:%d/does-not-exist.html' % self.PORT)
        self.assertEqual(r.text, "404, yay!\n")
