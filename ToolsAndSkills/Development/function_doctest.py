#
# Tools & Skills
#
# The Python Quants GmbH
#


def f(x):
    ''' Function to compute the square of a number.

    Parameters
    ==========
    x: float
        input number

    Returns
    =======
    y: float
        (positive) output number

    Raises
    ======
    ValueError if x is neither int nor float

    Examples
    ========
    >>> f(2)
    4

    >>> f(10)
    100

    >>> [f(x) for x in range(5)]
    [0, 1, 4, 9, 16]

    >>> f('python')
    Traceback (most recent call last):
        ...
    TypeError: Parameter must be integer or float.
    '''
    if type(x) not in [int, float]:
        raise TypeError('Parameter must be integer or float.')
    y = x ** 2
    return y


if __name__ == "__main__":
    import doctest
    doctest.testmod()
