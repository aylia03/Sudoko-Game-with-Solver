import unittest
from Cell import Cell


class MyTestCase(unittest.TestCase):
    def test_initial_value(self):
        cell = Cell()
        self.assertEqual(cell.value, 0)

    def test_set_value(self):
        cell = Cell()
        cell.set_value(8)
        self.assertEqual(cell.value, 8)
        self.assertNotIn(8, cell.possible_values)

    def test_value_not_possible(self):
        cell = Cell()
        with self.assertRaises(ValueError) as context:
            cell.set_value(100)

    def test_set_value_but_fixed(self):
        cell = Cell()
        with self.assertRaises(ValueError) as context:
            cell.fixed = True
            cell.set_value(1)

    def test_reset(self):
        cell = Cell()
        cell.set_value(8)
        self.assertNotIn(8, cell.possible_values)
        cell.reset()
        self.assertEqual(cell.value, 0)
        self.assertIn(8, cell.possible_values)

    def test_eliminate_possible_values(self):
        cell = Cell()
        cell.eliminate_possible_values(8)
        self.assertNotIn(8, cell.possible_values)

    def test_str_method(self):
        # Test __str__ method
        cell = Cell(value=5)
        self.assertEqual(str(cell), "5")  # Value is 5

        cell = Cell(value=0)
        self.assertEqual(str(cell), ".")  # Value is 0, should return "."

    def test_repr_method(self):
        # Test __repr__ method
        cell = Cell(value=5, fixed=True)
        cell.possible_values = {1, 2, 3}
        expected_repr = "Cell(value=5, fixed=True, possible_values={1, 2, 3})"
        self.assertEqual(repr(cell), expected_repr)

if __name__ == '__main__':
    unittest.main()
