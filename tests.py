import math
from fraction_definition import Fraction


if __name__ == '__main__':

    assert str(Fraction(3, 4)) == '3/4'
    assert Fraction(3/4) == Fraction('0.75') == Fraction(0.75) == Fraction('3/4')

    zero = Fraction(0)
    quarter = Fraction(0.25)
    half = Fraction(0.5)
    three_quarters = Fraction(0.75)
    one = Fraction(1)
    one_and_half = Fraction(1.5)
    two = Fraction(2)

    minus_half = Fraction(-0.5)
    minus_one = Fraction(-1)
    minus_two = Fraction(-2)



    assert Fraction() == zero

    # Equality
    assert half != one
    assert Fraction(50, 100) == half
    assert Fraction(200, 6) == Fraction(100, 3)
    assert Fraction(0.333) != Fraction(1, 3)

    # Arithmetic Operations
    assert three_quarters + half == one + quarter == Fraction(1.25)
    assert half - one == minus_half
    assert half * half == quarter
    assert half / half == one

    # String representation
    assert str(Fraction(3.13)) == '313/100'
    assert str(Fraction(50, 100)) == '1/2'

    # Assignment - by value
    f1 = half
    f1 /= half
    assert f1 == one
    assert half != one

    # Comparison Operators
    assert one < two
    assert two <= two
    assert one >= one

    # Math Operators
    assert abs(minus_one) == one
    assert math.ceil(half) == one
    assert math.floor(half) == zero