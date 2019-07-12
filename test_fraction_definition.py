from fraction_definition import Fraction
import pytest

Fraction('2')


class TestFraction:

    def test_str_float_initialization(self):
        fraction = Fraction('0.75')

        assert fraction.numerator == 3
        assert fraction.dinominator == 4

    def test_str_fraction_initialization(self):
        fraction = Fraction('3/4')

        assert fraction.numerator == 3
        assert fraction.dinominator == 4

    def test_pos_float_initialization(self):
        fraction = Fraction(0.75)

        assert fraction.numerator == 3
        assert fraction.dinominator == 4

    def test_neg_float_initialization(self):
        fraction = Fraction(-0.75)

        assert fraction.numerator == -3
        assert fraction.dinominator == 4

    def test_pos_int_initialization(self):
        fraction = Fraction(3)

        assert fraction.numerator == 3
        assert fraction.dinominator == 1

    def test_neg_int_initialization(self):
        fraction = Fraction(-1)

        assert fraction.numerator == -1
        assert fraction.dinominator == 1

    def test_zero_initialization(self):
        fraction = Fraction(0)

        assert fraction.numerator == 0
        assert fraction.dinominator == 1

    def test_empty_initialization(self):
        fraction = Fraction()

        assert fraction.numerator == 0
        assert fraction.dinominator == 1

    # equals
    def test_fraction_equals_assertion(self):
        assert Fraction(3 / 4) == Fraction(3 / 4)

    def test_int_equals_assertion(self):
        assert Fraction(2) == Fraction(2)

    def test_fraction_int_equals_assertion(self):
        assert Fraction(3) == Fraction(3 / 1)

    def test_fraction_float_equals_assertion(self):
        assert Fraction(1 / 2) == Fraction(0.5)

    def test_fraction_string_equals_assertion(self):
        assert Fraction(3 / 4) == Fraction('3 / 4')

    def test_int_string_equals_assertion(self):
        assert Fraction(2) == Fraction('2')

    def test_fraction_string_int_equals_assertion(self):
        assert Fraction(3) == Fraction('3 / 1')

    def test_fraction_string_float_equals_assertion(self):
        assert Fraction(1 / 2) == Fraction('0.5')

    # reduce
    def test_fraction_reduce_assertion(self):
        assert Fraction(200 / 6) == Fraction(100 / 3)

    def test_float_reduce_assertion(self):
        assert Fraction(0.5) == Fraction('4/8')

    # add
    def test_fraction_add_two_pos_assertion(self):
        assert Fraction(1) == Fraction(1 / 2) + Fraction(1 / 2)

    def test_fraction_add_two_diff_assertion(self):
        assert Fraction(3 / 4) == Fraction(1 / 1) + Fraction(-1 / 4)

    def test_int_add_two_pos_assertion(self):
        assert Fraction(2) == Fraction(1) + Fraction(1)

    def test_int_add_two_diff_assertion(self):
        assert Fraction(3) == Fraction(4) + Fraction(-1)

    def test_fraction_int_add_two_pos_assertion(self):
        assert Fraction(3 / 2) == Fraction(1) + Fraction(1 / 2)

    def test_fraction_int_add_two_diff_assertion(self):
        assert Fraction(3 / 4) == Fraction(1) + Fraction(-1 / 4)

    # sub
    def test_sub_two_pos_assertion(self):
        assert Fraction(0) == Fraction(1 / 2) - Fraction(1 / 2)

    def test_sub_two_diff_assertion(self):
        assert Fraction(-1) == Fraction(-1 / 2) - Fraction(1 / 2)

    # mul
    def test_mul_two_pos_assertion(self):
        assert Fraction(4) == Fraction(2) * Fraction(2)
        assert Fraction(1 / 4) == Fraction(1 / 2) * Fraction(1 / 2)

    def test_mul_two_diff_assertion(self):
        assert Fraction(1 / 4) == Fraction(-1 / 2) * Fraction(-1 / 2)

    def test_mul_with_zero_assertion(self):
        assert Fraction(0) == Fraction(1) * Fraction(0)

    # div
    def test_div_by_zero(self):
        res = pytest.raises(Exception, Fraction.__truediv__, Fraction(1), Fraction(0))
        assert "Divide by Zero" in str(res.value)

    def test_div_two_pos_assertion(self):
        assert Fraction(1 / 2) == Fraction(1 / 4) / Fraction(1 / 2)

    def test_div_two_diff_assertion(self):
        Fraction(-1 / 4) / Fraction(-1 / 2)
        assert Fraction(-1 / 2) == Fraction(-1 / 4) / Fraction(1 / 2)

    def test_div_two_diff_assertion(self):
        assert Fraction(1 / 2) == Fraction(-1 / 4) / Fraction(-1 / 2)

    # lt
    def test_less_than_two_pos_assertion(self):
        assert Fraction(1 / 4) < Fraction(1 / 2)

    def test_less_than_diff_pos_assertion(self):
        assert Fraction(-1 / 2) < Fraction(1 / 4)

    # lte
    def test_less_than_equal_two_pos_assertion(self):
        assert Fraction(1 / 4) <= Fraction(1 / 2)

    def test_less_than_equal_diff_pos_assertion(self):
        assert Fraction(-1 / 2) <= Fraction(-1 / 2)

    # gt
    def test_greater_than_two_pos_assertion(self):
        assert Fraction(1 / 2) > Fraction(1 / 4)

    def test_greater_than_diff_pos_assertion(self):
        assert Fraction(1 / 4) > Fraction(-1 / 2)

    # gte
    def test_greater_than_equal_two_pos_assertion(self):
        assert Fraction(1 / 2) >= Fraction(1 / 4)

    def test_greater_than_equal_diff_pos_assertion(self):
        assert Fraction(-1 / 2) >= Fraction(-1 / 2)

    # abs
    def test_abs_neg_int_assertion(self):
        assert Fraction(1) == Fraction.__abs__((Fraction(-1)))

    def test_abs_num_neg_fraction_assertion(self):
        assert Fraction(1 / 2) == Fraction.__abs__(Fraction(-1 / 2))

    def test_abs_din_neg_fraction_assertion(self):
        assert Fraction(1 / 2) == Fraction.__abs__(Fraction(1 / -2))

    # ceil
    def test_ceil_pos_assertion(self):
        assert Fraction(1) == Fraction.__ceil__(Fraction(3 / 4))

    def test_ceil_neg_assertion(self):
        assert Fraction(0) == Fraction.__ceil__(Fraction(-3 / 4))

    def test_ceil_pos_int_assertion(self):
        assert Fraction(2)==Fraction.__ceil__(Fraction(2))

    # floor
    def test_floor_pos_assertion(self):
        assert Fraction(0) == Fraction.__floor__(Fraction(3 / 4))

    def test_floor_neg_assertion(self):
        assert Fraction(-1) == Fraction.__floor__(Fraction(-3 / 4))

    def test_floor_pos_int_assertion(self):
        assert Fraction(2)==Fraction.__floor__(Fraction(2))
