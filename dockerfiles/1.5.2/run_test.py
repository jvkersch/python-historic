#!/usr/bin/env python3

import os
import shutil
import subprocess
import tempfile
import unittest

TEST_SCRIPT = """\
import sys
print sys.version
"""

TAG = "jvkersch/python-historic:1.5.2"


class TestImage(unittest.TestCase):

    def test_version(self):
        # Given
        folder, script = self._write_test_script()

        # When
        output = self._run_docker_command(
            ["-it",
             "--rm",
             "-v", "{}:/usr/src/testapp".format(folder),
             "-w", "/usr/src/testapp",
             TAG,
             "python",
             script]
        )

        # Then
        self.assertRegex(output, "^1.5.2")

    def _write_test_script(self):
        d = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, d)

        fname = os.path.join(d, "script.py")
        with open(fname, "wt") as fp:
            fp.write(TEST_SCRIPT)

        return d, "script.py"

    def _run_docker_command(self, params):
        cmd = ["docker", "run"]
        proc = subprocess.run(
            cmd + params,
            check=True,
            stdout=subprocess.PIPE,
            encoding="ascii",
        )

        return proc.stdout


if __name__ == '__main__':
    unittest.main()
