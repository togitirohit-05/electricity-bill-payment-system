import unittest
from billing import calculateBill


class TestBilling(unittest.TestCase):
    def test_units_within_free_limit(self):
        self.assertEqual(calculateBill(50), 0)

    def test_units_in_first_slab(self):
        self.assertEqual(calculateBill(150), 250)

    def test_units_in_second_slab(self):
        self.assertEqual(calculateBill(300), 1200)

    def test_units_in_third_slab(self):
        self.assertEqual(calculateBill(450), 2400)


if __name__ == '__main__':
    unittest.main()
