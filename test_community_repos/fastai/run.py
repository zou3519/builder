import unittest
import re
import subprocess
import sys
import argparse

PY3 = sys.version_info >= (3, 0)

def run(command):
    """
    Returns (return-code, stdout, stderr)
    """
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    rc = p.returncode
    if PY3:
        output = output.decode("ascii")
        err = err.decode("ascii")
    return (rc, output, err)


class TestFastai(unittest.TestCase):
    pass


def _test(cls, directory, ipynb_file):
    (rc, out, err) = run(
            "jupyter nbconvert --execute {}/{}".format(directory, ipynb_file))
    cls.assertEqual(rc, 0, "stdout:\n{}\nstderr:\n{}".format(out, err))


(rc, stdout, stderr) = run("find . -type f | grep -P '.ipynb$'")
if rc is not 0:
    print("Couldn't execute find and/or grep")
    exit(1)

def test_name(ipynb_file):
    filename = ipynb_file.split('.')[0]
    return "test_{}".format(filename)

files = stdout.split('\n')
files = [f for f in files if len(f) > 0]
dirs_files = [f.rsplit('/', 1) for f in files]
for (d, f) in dirs_files:
    setattr(TestFastai, test_name(f), 
            classmethod(lambda cls: _test(cls(), d, f)))


if __name__ == '__main__':
    unittest.main()
