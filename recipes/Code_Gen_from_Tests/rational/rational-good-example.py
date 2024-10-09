# Insert the generated Rational class here.
# Don't include the test code or any markdown or other text included in the generated output!
# Include appropriate import statements, e.g., you may see the generated code calls `gcd` (for
# greatest common divisor, which would require this import `from math import gcd`.

from math import gcd

class Rational:
    """
    A class representing rational numbers.

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