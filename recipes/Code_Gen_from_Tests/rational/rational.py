from math import gcd

class Rational:
    """
    A class representing rational numbers. Note this implementation doesn't cover any 
    algebraic operations, because the tests don't cover them either. This is left as
    an exercise for you to do ;) However, it does correctly divide the numerator and
    denominator by their greatest common divisor, "M", e.g., 
    N/D == (M*N')/(M*D') == N'/D'

    Attributes:
        numerator (int): The numerator of the rational number.
        denominator (int): The denominator of the rational number.

    Methods:
        __init__(self, numerator, denominator): Initializes a Rational object with the given numerator and denominator.
        __str__(self): Returns a string representation of the Rational object.
        __eq__(self, other): Checks if two Rational objects are equal.
    """

    def __init__(self, numerator, denominator):
        """
        Initializes a Rational object with the given numerator and denominator.

        Args:
            numerator (int): The numerator of the rational number.
            denominator (int): The denominator of the rational number.

        Raises:
            ValueError: If the denominator is zero.
        """
        if denominator == 0:
            raise ValueError("Cannot create a Rational with a zero denominator.")

        divisor = gcd(numerator, denominator)
        self.numerator = numerator // divisor
        self.denominator = denominator // divisor

    def __str__(self):
        """
        Returns a string representation of the Rational object.

        Returns:
            str: A string representation of the Rational object in the form "numerator/denominator".
        """
        return f"{self.numerator}/{self.denominator}"

    def __eq__(self, other):
        """
        Checks if two Rational objects are equal.

        Args:
            other (Rational): The other Rational object to compare with.

        Returns:
            bool: True if the two Rational objects are equal, False otherwise.
        """
        return self.numerator * other.denominator == self.denominator * other.numerator