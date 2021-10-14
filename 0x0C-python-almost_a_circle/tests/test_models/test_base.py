#!/usr/bin/python3
"""Base unittests module"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Base unittest class"""
    def test_arg(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b2.id-1)
        self.assertEqual(b1.id, b3.id-2)

    def test_None(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)
