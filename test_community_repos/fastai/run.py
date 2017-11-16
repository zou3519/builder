import unittest
import subprocess
import sys

PY3 = sys.version_info >= (3, 0)


def run(command):
    """
    Returns (return-code, stdout, stderr)
    """
    p = subprocess.Popen(command, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    rc = p.returncode
    if PY3:
        output = output.decode("ascii")
        err = err.decode("ascii")
    return (rc, output, err)


class TestFastai(unittest.TestCase):
    pass


def test_name(ipynb_file):
    filename = ipynb_file.split('.')[0]
    return "test_{}".format(filename)


def _test(cls, directory, ipynb_file):
    (rc, out, err) = run(
            "jupyter nbconvert --execute {}/{}".format(directory, ipynb_file))
    cls.assertEqual(rc, 0, "stdout:\n{}\nstderr:\n{}".format(out, err))


# Generate the tests, one for each ipynb file
# Only tests the following:
# everything in tutorials/*
# courses/dl1/* files that start with lesson1
(rc, stdout, stderr) = run(
        "find . -type f | grep -P '(courses/dl1/lesson1|tutorials/).+.ipynb$'")
if rc is not 0:
    print("Couldn't execute find and/or grep")
    exit(1)

files = stdout.split('\n')
files = [f for f in files if len(f) > 0]
for f in files:
    print("found {}".format(f))
dirs_files = [f.rsplit('/', 1) for f in files]
for (d, f) in dirs_files:
    setattr(TestFastai, test_name(f),
            lambda cls, d=d, f=f: _test(cls, d, f))


if __name__ == '__main__':
    unittest.main()
