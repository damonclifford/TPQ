#
# Tools & Skills
#
# The Python Quants GmbH
#
import unittest


def f(x):
    ''' Docstring here. '''
    if type(x) not in [int, float]:
        raise TypeError('Parameter must be integer or float.')
    y = x ** 2
    return y


class TestFunction(unittest.TestCase):

    def test_square(self):
        self.assertEqual(f(2), 4)
        self.assertEqual(f(10), 100)
        self.assertEqual([f(x) for x in range(5)],
                         [0, 1, 4, 9, 16])

    def test_true(self):
        self.assertTrue(f(2) == 4)
        self.assertFalse(f(4) == 15)

    def test_error(self):
        with self.assertRaises(TypeError):
            f('python')


if __name__ == "__main__":
    unittest.main()
