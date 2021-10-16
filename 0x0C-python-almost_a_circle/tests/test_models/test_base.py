#!/usr/bin/python3
"""Base unittests module"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Base unittest class"""

    def test_None(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_instances(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b2.id-1)
        self.assertEqual(b1.id, b3.id-2)

    def test_two_instances(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id-1)

    def test_id_public(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_private_instance(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_float_id(self):
        self.assertEqual(5.5, Base(5.5).id)

    def test_complex_id(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2, 3), Base((1, 2, 3)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_id(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def test_bytes_id(self):
        self.assertEqual(b'Paul', Base(b'Paul').id)

    def test_bytearray_id(self):
        self.assertEqual(bytearray(b'Python'), Base(bytearray(b'Python')).id)

    def test_memoryview_id(self):
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_double_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)
