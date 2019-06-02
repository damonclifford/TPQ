#
# Fibonacci Numbers
#
# [0,] 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ... 
#
import q
import doctest
import unittest

def fibonacci(n):
    ''' Calculating Fibonacci Numbers.
    Examples
    ========
    >>> fibonacci(3)
    2
    >>> fibonacci(9)
    34
    >>> fibonacci(100)
    354224848179261915075
    >>> fibonacci('python')
    Traceback (most recent call last):
	...
    TypeError: n must be of type int.
    '''
    if type(n) != int:
        raise TypeError('n must be of type int.')
    a, b = 0, 1
    for _ in range(1, n + 1):
        a, b = b, a + b
    return a

class TestFibonacci(unittest.TestCase):
    def test_single(self):
        self.assertEqual(fibonacci(9), 34)
    def test_bool(self):
        self.assertTrue(fibonacci(3) == 2)
    def test_error(self):
        with self.assertRaises(TypeError) as f:
            fibonacci('python')

if __name__ is '__main__':
    print('It is running.')
    fn = fibonacci(125)
    q(fn)
    # q.d()
    doctest.testmod()
    unittest.main()
