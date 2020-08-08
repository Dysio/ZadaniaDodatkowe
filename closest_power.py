def closest_power(base, num):
    """
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    """
    pass
if __name__ == '__main__':
    assert closest_power(4, 12) == 2
    assert closest_power(3, 12) == 2
    assert closest_power(4, 1) == 0