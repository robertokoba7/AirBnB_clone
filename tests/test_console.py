#!/usr/bin/python3
"""Test module for console """

import console
import unittest
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import pep8
HBNBCommand = console.HBNBCommand


class TestConsole(unitteat.TestCase):
    """Test console: will test the pep8 and docstring"""

    def test_base_pep8_conformance_console(self):
        """Test that we conform to pep8"""

        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0)

    def test_base_pep8_conformance_consoletest(self):
        """Test that we conform to pep8 """

        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./test/test_console.py'])
        self.assertEqual(result.total_errors, 0)

    def test_console_docstring(self):
        """Test docstring """
        self.assertIsNot(console.__doc__,None,
                'console.py needs a docstring')
        self.assertTrue(len(console.__doc___) >= 1,
                "console.py needs a docstring")

    def test_HBNBCommand_docstring(self):
        """Test command interpreter docstring """

        self.assertIsNot(HBNBCommand.__doc__, None,
                'console.py needs a docstring')
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                'console.py needs a docstring')
