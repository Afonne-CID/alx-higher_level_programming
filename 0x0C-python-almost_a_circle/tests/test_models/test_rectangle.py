import unittest
import sys
import io
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class.
    """
    def test_rectangle_is_base_instance(
            self):
        self.assertIsInstance(Rectangle(3, 10), Base)

    def test_without_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r1 = Rectangle(10, 2, 2)
        r2 = Rectangle(2, 2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        self.assertEqual(5, Rectangle(1, 2, 3, 4, 5).id)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 5, 7, 9, 1).__width)

    def test_height_priave(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 5, 7, 9, 1).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 5, 7, 9, 1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 5, 7, 9, 1).__y)

    def test_width_getter(self):
        r = Rectangle(10, 12, 7, 5, 1)
        self.assertEqual(10, r.width)

    def test_height_getter(self):
        r = Rectangle(5, 12, 7, 5, 1)
        self.assertEqual(12, r.height)

    def test_width_setter(self):
        r = Rectangle(5, 12, 7, 5, 1)
        r.width = 7
        self.assertEqual(7, r.width)

    def test_height_setter(self):
        r = Rectangle(5, 12, 7, 5, 1)
        r.height = 20
        self.assertEqual(20, r.height)

    def test_x_getter(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(3, r.x)

    def test_y_getter(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(4, r.y)

    def test_x_setter(self):
        r = Rectangle(1, 3, 4, 6, 4)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_y_setter(self):
        r = Rectangle(1, 3, 4, 6, 4)
        r.y = 19
        self.assertEqual(19, r.y)


class TestRectangle_width(unittest.TestCase):
    """Unittests for testing initialization of Rectangle's width attribute.
    """

    def test_None_value(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("String", 2)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(7.9, 1)

    def test_complex_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(5), 2)

    def test_set_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2}, 1)

    def test_complex_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(2), 2)

    def test_dict_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 1, "b": 2}, 2)

    def test_bool_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2], 7)

    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2), 7)

    def test_frozenset_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({1, 2, 3}), 7)

    def test_range_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(10), 2)

    def test_bytes_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'Python', 2)

    def test_bytearray_with(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b'abcd'), 7)

    def test_memoryview_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b'abcd'), 7)

    def test_inf_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 7)

    def test_nan_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 7)

    def test_negative_value_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-7, 2)

    def test_zero_with(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)


class TestRectangle_height(unittest.TestCase):
    """Unittests for testing initialization of Rectangle's height attribute
    """

    def test_None_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, None)

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "String")

    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, 5.5)

    def test_complex_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, complex(5))

    def test_dict_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {"a": 1, "b": 2})

    def test_set_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {1, 2, 3})

    def test_bool_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, False)

    def test_list_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, [1, 2, 3])

    def test_typle_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, (1, 2, 3))

    def test_frozenset_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, frozenset({2, 2, 4}))

    def test_range_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, range(2))

    def test_bytes_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(7, b'Python')

    def test_bytearray_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, bytearray(b'abcd'))

    def test_memoryview_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, memoryview(b'Python'))

    def test_inf_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, float('inf'))

    def test_nan_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, float('nan'))

    def test_negative_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(7, -1)

    def test_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(7, 0)


class TestRectangle_x(unittest.TestCase):
    """Unittests for testing initialization of Rectangle x attribute
    """

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, "string")

    def test_int__x(self):
        self.assertEqual(2, Rectangle(2, 3, 2).x)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, 5.5)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, complex(5))

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, {"a": 1, "b": 2})

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, {1, 2, 3})

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, True)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, [1, 2, 3])

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, (1, 2, 3))

    def test_frozenset_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, frozenset({1, 3, 3}))

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, range(5))

    def test_bytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, b'Python')

    def test_bytearray_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, bytearray(b'abcd'))

    def test_memoryview_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, memoryview(b'abcd'))

    def test_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, float('inf'))

    def test_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, float('nan'))

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(2, 3, -1, 2)

    def test_zero_x(self):
        self.assertEqual(0, Rectangle(2, 3, 0, 2).x)


class TestRectangle_y(unittest.TestCase):
    """Unittests for testing initialization of Rectangle y attribute."""

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, "invalid")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 5.5)

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, complex(5))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {"a": 1, "b": 2})

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, [1, 2, 3])

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {1, 2, 3})

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, (1, 2, 3))

    def test_frozenset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, frozenset({1, 2, 3, 1}))

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, range(5))

    def test_bytes_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, b'Python')

    def test_bytearray_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, bytearray(b'abcdefg'))

    def test_memoryview_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, memoryview(b'abcedfg'))

    def test_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float('inf'))

    def test_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float('nan'))

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 5, 0, -1)


class TestRectangle_order_of_initialization(unittest.TestCase):
    """Unittests for testing Rectangle's order of attributes initialization
    """

    def test_width_before_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("String", "Invalid")

    def test_height_before_x(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "Invalid", "Invalid")

    def test_width_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("Invalid", 2, "String")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "x string", "invalid y")


class TestRectangle_area(unittest.TestCase):
    """Unittests for testing the area method of the Rectangle class
    """

    def test_area_small_nos(self):
        r = Rectangle(7, 2, 1, 1)
        self.assertEqual(14, r.area())

    def test_area_large_nos(self):
        r = Rectangle(999999999999999, 99999999999999, 1, 1, 1)
        self.assertEqual(99999999999998900000000000001, r.area())

    def test_change_attribute_values(self):
        r = Rectangle(7, 2, 1, 1)
        r.width = 10
        r.height = 10
        self.assertEqual(100, r.area())

    def test_one_arg_area(self):
        r = Rectangle(7, 2, 1, 1)
        with self.assertRaises(TypeError):
            r.area(2)


class TestRectangle_display(unittest.TestCase):
    """Unittests for testing Rectangle's display method and __str__"""

    @staticmethod
    def capture_stdout(rect, method):
        """Captures and returns text printed to stdout.

        Args:
            rect (Rectangle): The Rectangle to print to stdout.
            method (str): The method to run on react.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    """Test __str__method"""
    def test_str_method_print_width_height(self):
        r = Rectangle(4, 6)
        capture = TestRectangle_display.capture_stdout(r, "print")
        correct = "[Rectangle] ({}) 0/0 - 4/6\n".format(r.id)
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_width_height_x(self):
        r = Rectangle(5, 5, 1)
        correct = "[Rectangle] ({}) 1/0 - 5/5".format(r.id)
        self.assertEqual(correct, r.__str__())

    def test_str_method_width_height_x_y(self):
        r = Rectangle(1, 8, 2, 4)
        correct = "[Rectangle] ({}) 2/4 - 1/8".format(r.id)
        self.assertEqual(correct, str(r))

    def test_str_method_width_height_x_y_id(self):
        r = Rectangle(13, 21, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(r))

    def test_str_method_changed_attributes(self):
        r = Rectangle(7, 7, 0, 0, [4])
        r.width = 15
        r.height = 1
        r.x = 8
        r.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(r))

    def test_str_method_one_arg(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.__str__(1)

    """Test display() method"""
    def test_display_width_height(self):
        r = Rectangle(2, 3, 0, 0, 0)
        capture = TestRectangle_display.capture_stdout(r, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())

    def test_display_width_height_x(self):
        r = Rectangle(3, 2, 1, 0, 1)
        capture = TestRectangle_display.capture_stdout(r, "display")
        self.assertEqual(" ###\n ###\n", capture.getvalue())

    def test_display_width_height_y(self):
        r = Rectangle(4, 5, 0, 1, 0)
        capture = TestRectangle_display.capture_stdout(r, "display")
        self.assertEqual("\n####\n####\n####\n####\n####\n",
                         capture.getvalue())

    def test_display_with_height_x_y(self):
        r = Rectangle(2, 4, 3, 2, 0)
        capture = TestRectangle_display.capture_stdout(r, "display")
        self.assertEqual("\n\n   ##\n   ##\n   ##\n   ##\n",
                         capture.getvalue())

    def test_display_with_one_arg(self):
        r = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            r.display(1)


class TestRectangle_update_args(unittest.TestCase):
    """Unittests for testing update method of the Rectangle class
    """

    def test_update_no_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_one_arg(self):
        r = Rectangle(12, 1, 3, 4, 5)
        r.update(20)
        self.assertEqual("[Rectangle] (20) 3/4 - 12/1", str(r))

    def test_update_two_args(self):
        r = Rectangle(12, 1, 3, 4, 5)
        r.update(20, 2)
        self.assertEqual("[Rectangle] (20) 3/4 - 2/1", str(r))

    def test_update_three_args(self):
        r = Rectangle(12, 1, 3, 4, 5)
        r.update(20, 2, 3)
        self.assertEqual("[Rectangle] (20) 3/4 - 2/3", str(r))

    def test_update_four_args(self):
        r = Rectangle(12, 1, 3, 4, 5)
        r.update(20, 2, 3, 6)
        self.assertEqual("[Rectangle] (20) 6/4 - 2/3", str(r))

    def test_update_five_args(self):
        r = Rectangle(12, 1, 3, 4, 5)
        r.update(20, 2, 3, 6, 10)
        self.assertEqual("[Rectangle] (20) 6/10 - 2/3", str(r))

    def test_update_more_than_five_args(self):
        r = Rectangle(12, 1, 3, 4, 5)
        r.update(20, 2, 3, 6, 10, 9)
        self.assertEqual("[Rectangle] (20) 6/10 - 2/3", str(r))

    def test_update_None_args(self):
        r = Rectangle(12, 1, 3, 4, 5)
        r.update(None, 4, 5, 2)
        correct = "[Rectangle] ({}) 2/4 - 4/5".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_twice(self):
        r = Rectangle(12, 1, 3, 4, 5)
        r.update(89, 2, 3, 4, 5, 6)
        r.update(6, 5, 4, 3, 2, 89)
        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(r))

    def test_update_args_invalid_width(self):
        r = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "string")

    def test_update_arg_width_zero(self):
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, 0)

    def test_update_args_width_negative(self):
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, -1)

    def test_update_args_height_invalid(self):
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 4, "string")

    def test_update_args_height_zero(self):
        r = Rectangle(5, 5, 5, 5, 5,)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 2, 0)

    def test_update_args_height_negative(self):
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 2, -2)

    def test_update_args_x_invalid(self):
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 2, 4, "string")

    def test_update_args_x_zero(self):
        r = Rectangle(5, 5, 5, 5, 5)
        r.update(89, 2, 1, 0)
        self.assertEqual(0, r.x)

    def test_update_args_x_negative(self):
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(89, 2, 3, -2)

    def test_update_args_y_invalid(self):
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(89, 2, 3, 4, "string")

    def test_update_args_y_zero(self):
        r = Rectangle(5, 5, 5, 5, 5,)
        r.update(89, 2, 3, 4, 0)
        self.assertEqual(0, r.y)

    def test_update_args_y_negative(self):
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(89, 2, 3, 4, -2)

    """ Test initialization """
    def test_update_args_width_before_height(self):
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "string", "invalid")

    def test_update_args_height_before_x(self):
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 10, "string", "invalid")

    def test_update_args_width_before_x(self):
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "string", 5, "invalid")

    def test_update_args_x_before_y(self):
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 2, 10, "sgring", "invalid")

    def test_update_args_width_before_y(self):
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "string", 10, 2, "invalid")

    def test_update_args_height_before_y(self):
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 10, "strng", 10, "invalid")

class TestRectangle_update_kwargs(unittest.TestCase):
    """Unittests for testing update kwargs method of the Rectangle class.
    """

    def test_update_kwargs_one(self):
        r = Rectangle(5, 5, 5, 5, 5)
        r.update(id=1)
        self.assertEqual("[Rectangle] (1) 5/5 - 5/5", str(r))

    def test_update_kwargs_two(self):
        r = Rectangle(5, 5, 5, 5, 5)
        r.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 5/5 - 2/5", str(r))

    def test_update_kwargs_three(self):
        r = Rectangle(5, 5, 5, 5, 5)
        r.update(width=2, height=3, id=2)
        self.assertEqual("[Rectangle] (2) 5/5 - 2/3", str(r))

    def test_update_kwargs_foure(self):
        r = Rectangle(5, 5, 5, 5, 5)
        r.update(width=2, height=3, id=2, x=10)
        self.assertEqual("[Rectangle] (2) 10/5 - 2/3", str(r))

    def test_update_kwargs_five(self):
        r = Rectangle(5, 5, 5, 5, 5)
        r.update(width=2, height=3, id=2, x=10, y=12)
        self.assertEqual("[Rectangle] (2) 10/12 - 2/3", str(r))

    def test_update_kwargs_None_id(self):
        r = Rectangle(5, 5, 5, 5, 5)
        r.update(id=None)
        correct = "[Rectangle] ({}) 5/5 - 5/5".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_None_plus(self):
        r = Rectangle(5, 5, 5, 5, 5)
        r.update(id=None, height=7, y=9)
        correct = "[Rectangle] ({}) 5/9 - 5/7".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_twice(self):
        r = Rectangle(5, 5, 5, 5, 5)
        r.update(id=89, x=1, height=2)
        r.update(y=3, height=15, width=2)
        self.assertEqual("[Rectangle] (89) 1/3 - 2/15", str(r))

    def test_update_kwargs_width_type(self):
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="string")

    def test_update_kwargs_width_zero(self):
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)

    def test_update_kwargs_width_negative(self):
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-2)

    def test_update_kwargs_height_type(self):
        r = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="string")

    def test_update_kwargs_height_zero(self):
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)

    def test_update_kwargs_height_negative(self):
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-2)

    def test_update_kwargs_invalid_x_type(self):
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-2)

    def test_update_kwargs_invalid_y_type(self):
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="string")

    def test_update_kwargs_x_negative(self):
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-1)

    """Testing ``args`` and ``kwargs`` together"""
    def test_update_args_and_kwargs_with_args_first(self):
        r = Rectangle(5, 5, 5, 5, 5)
        r.update(89, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (89) 5/5 - 2/5", str(r))

    def test_update_args_and_kwargs_with_only_kwargs(self):
        r = Rectangle(5, 5, 5, 5, 5)
        r.update(height=10, x=17)
        self.assertEqual("[Rectangle] (5) 17/5 - 5/10", str(r))

    def test_update_kwargs_wrong_keys(self):
        r = Rectangle(5, 5, 5, 5, 5)
        r.update(a=5, b=10)
        self.assertEqual("[Rectangle] (5) 5/5 - 5/5", str(r))

    def test_update_kkwargs_some_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(height=5, id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Rectangle] (89) 19/7 - 10/5", str(r))
