import unittest

from app.utils import calculate_optimal_route


class OptimalRouteTestCase(unittest.TestCase):

    def test_calculate_optimal_route(self):
        points = [
            {'lat': 10, 'lng': 20},
            {'lat': 30, 'lng': 40},
            {'lat': 50, 'lng': 60},
            {'lat': 70, 'lng': 80},
        ]

        expected_route = [0, 1, 2, 3, 0]

        actual_route = calculate_optimal_route(points)

        self.assertEqual(actual_route, expected_route)
