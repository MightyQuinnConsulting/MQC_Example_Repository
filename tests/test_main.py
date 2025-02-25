# Unit test for main.py
import unittest
from subprocess import check_output

def test_hello_world():
    output = check_output(["python", "src/main.py"]).decode("utf-8").strip()
    assert output == "Hello, World!"
