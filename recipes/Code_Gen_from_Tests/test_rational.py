# Example unit tests using Hypothesis for property-based testing.
# Adapted from: https://github.com/deanwampler/tdd-hypothesis-example
# Hypothesis website: https://hypothesis.readthedocs.io/en/latest/

from hypothesis import given, strategies as st
import unittest
from rational import Rational
from math import gcd

class TestRational(unittest.TestCase):
    """
    Test the features implemented curently by Rational.
    Add new tests for Rational arithmetic operations, like multiplication and addition,
    watch the test fail, then implement the feature and ensure the test now passes.
    See also other properties described in the Rational Wikipedia page:
    https://en.wikipedia.org/wiki/Rational_number
    
    Also, try adding a second way to construct Rationals that accepts a string
    argument, "M/N". (Now you really have to think about handling input errors!) 
    What are the requirements for valid strings, e.g., for "M" and "N"?
    If an invalid string is provided, how should the error be handled?
    """

    # Disallow zero for the demoninator!

    nonzero_integers = st.integers().filter(lambda i: i != 0)

    @given(st.integers(), nonzero_integers)
    def test_init_takes_numerator_denominator(self, numer, denom):
        """
        A "relatively-trivial" test, but note that the returned
        numerator and denominator will be divided by their greatest
        common divisor.
        """
        rat = Rational(numer, denom)
        divisor = gcd(numer, denom)
        self.assertEqual(numer // divisor, rat.numerator)
        self.assertEqual(denom // divisor, rat.denominator)

    @given(st.integers())
    def test_zero_denominator_raises(self, numer):
        """
        Don't allow zero for the denominator!!
        """
        with self.assertRaises(ValueError):
            rat = Rational(numer, 0)

    @given(st.integers(), nonzero_integers)
    def test_a_rational_equals_itself(self, numer, denom):
        """
        This test passes without adding a custom __eq__ method. 
        Without the __eq__ method, would this test actually use
        "logical" instance equality or just locations in memory?
        """
        rat = Rational(numer, denom)
        self.assertEqual(rat, rat)

    @given(st.integers(), nonzero_integers)
    def test_identical_rationals_are_equal(self, numer, denom):
        """
        Would this one pass if we deleted (or commented out) our custom __eq__ method? 
        Try it!
        """
        rat1 = Rational(numer, denom)
        rat2 = Rational(numer, denom)
        self.assertEqual(rat1, rat2)

    @given(st.integers(), nonzero_integers, nonzero_integers)
    def test_equality_for_two_rationals_with_num_and_dom_that_are_multiples_of_each_other(self, numer, denom, multiple):
        """
        Rule: a/b == c/d iff ad == bc
        Since a*M/b*M == a/b, then a*M/b*M == c/d
        """
        rat1 = Rational(numer*multiple, denom*multiple)
        rat2 = Rational(numer, denom)
        self.assertEqual(rat1, rat2)

    @given(st.integers(), nonzero_integers, st.integers(), nonzero_integers)
    def test_two_non_identical_rationals_are_not_equal_to_each_other(self, numer1, denom1, numer2, denom2):
        """
        Rule: a/b == c/d iff ad == bc
        This is a better test, because it randomly generates different instances.
        However, the test has to check for the case where the two values happen to be
        equivalent!
        """
        rat1 = Rational(numer1, denom1)
        rat2 = Rational(numer2, denom2)
        if numer1*denom2 == numer2*denom1:
            self.assertEqual(rat1, rat2)
        else:
            self.assertNotEqual(rat1, rat2)

if __name__ == "__main__":
    unittest.main()