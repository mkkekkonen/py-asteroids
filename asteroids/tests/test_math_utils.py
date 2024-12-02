'''
This module contains the unit tests for the math_utils module.
'''

import unittest

from ..utils.math_utils import get_point_on_circle, is_point_on_right_side_of_line


class TestMathUtils(unittest.TestCase):
    '''
    This class contains the unit tests for the math_utils module.
    '''

    def test_get_point_on_circle(self):
        '''
        This method tests the get_point_on_circle function.
        '''
        center = (0, 0)
        radius = 10
        angle = 0
        expected = (10, 0)
        self.assertEqual(get_point_on_circle(center, radius, angle), expected)

        center = (0, 0)
        radius = 10
        angle = 90
        expected = (0, 10)
        self.assertEqual(get_point_on_circle(center, radius, angle), expected)

    def test_is_point_on_right_side_of_line(self):
        '''
        This method tests the is_point_on_right_side_of_line function.
        '''
        start_point = (0, 0)
        end_point = (10, 0)
        point = (5, 5)
        self.assertTrue(is_point_on_right_side_of_line(
            start_point, end_point, point))

        start_point = (0, 0)
        end_point = (10, 0)
        point = (5, -5)
        self.assertFalse(is_point_on_right_side_of_line(
            start_point, end_point, point))
