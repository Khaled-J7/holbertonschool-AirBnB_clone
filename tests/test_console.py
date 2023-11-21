import unittest
from unittest.mock import patch
from io import StringIO
import sys
from console import HBNBCommand


class TestHBNBCommandMethods(unittest.TestCase):
    def setUp(self):
        """Set up the HBNBCommand instance for testing"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Tear down after testing"""
        pass

    def capture_output(self, func, *args):
        """Capture the output of the function execution"""
        captured_output = StringIO()
        sys.stdout = captured_output
        func(*args)
        sys.stdout = sys.__stdout__
        return captured_output.getvalue().strip()

    def test_quit_command(self):
        """Test quit command"""
        self.assertTrue(self.console.do_quit(""))
