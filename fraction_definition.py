import math


class Fraction:

    def __init__(self, *args):

        self.numerator = 0
        self.dinominator = 1

        if len(args) == 0:
            pass

        if len(args) == 2:
            self.numerator, self.dinominator = self.reduce(args[0], args[1])

        if len(args) == 1:

            if type(args[0]) == str and args[0].__contains__('.'):
                temp = args[0].split('.')

                self.numerator = int(temp[0] + temp[1])
                self.dinominator = 10 ** len(temp[1])

                self.numerator, self.dinominator = self.reduce(self.numerator, self.dinominator)

            elif type(args[0]) == str and args[0].__contains__('/'):
                temp = list(map(int, args[0].split('/')))
                self.numerator, self.dinominator = self.reduce(temp[0], temp[1])

            elif type(args[0]) == str:

                self.numerator = int(args[0])

            if type(args[0]) == int:
                self.numerator = args[0]
                self.dinominator = 1
                self.numerator, self.dinominator = self.reduce(self.numerator, self.dinominator)

            if type(args[0]) == float:
                temp = str(args[0])
                temp = temp.split('.')

                self.numerator = int(temp[0] + temp[1])
                self.dinominator = 10 ** len(temp[1])
                self.numerator, self.dinominator = self.reduce(self.numerator, self.dinominator)

    def reduce(self, nume, din):

        gcd = math.gcd(nume, din)

        nume = nume / gcd
        din = din / gcd

        if nume < 0 and din < 0:
            nume *= -1
            din *= -1
        return int(nume), int(din)

    def __eq__(self, other):

        if self.numerator == other.numerator and self.dinominator == other.dinominator:

            return True
        else:

            return False

    def __add__(self, other):

        num = self.numerator * other.dinominator + other.numerator * self.dinominator
        din = self.dinominator * other.dinominator

        num, din = self.reduce(num, din)

        return Fraction(num, din)

    def __sub__(self, other):

        num = self.numerator * other.dinominator - other.numerator * self.dinominator
        din = self.dinominator * other.dinominator

        num, din = self.reduce(num, din)

        return Fraction(num, din)

    def __mul__(self, other):

        num = self.numerator * other.numerator
        din = self.dinominator * other.dinominator

        num, din = self.reduce(num, din)

        return Fraction(num, din)

    def __truediv__(self, other):

        if other.numerator == 0:
            raise Exception("Divide by Zero")

        num = self.numerator * other.dinominator
        din = self.dinominator * other.numerator

        num, din = self.reduce(num, din)

        return Fraction(num, din)

    def __lt__(self, other):

        if self.numerator * other.dinominator < self.dinominator * other.numerator:

            return True
        else:

            return False

    def __le__(self, other):

        if self.numerator * other.dinominator <= self.dinominator * other.numerator:

            return True
        else:

            return False

    def __gt__(self, other):

        if self.numerator * other.dinominator > self.dinominator * other.numerator:

            return True
        else:

            return False

    def __ge__(self, other):

        if self.numerator * other.dinominator >= self.dinominator * other.numerator:

            return True
        else:

            return False

    def __str__(self):

        return str(self.numerator) + '/' + str(self.dinominator)

    def __abs__(self):

        num = self.numerator
        din = self.dinominator

        if self.numerator < 0:
            num = -1 * self.numerator

        if self.dinominator < 0:
            din = -1 * self.dinominator

        return Fraction(num, din)

    def __ceil__(self):

        num = int(math.ceil(self.numerator / self.dinominator))
        # num = int(self.numerator / self.dinominator) + 1
        din = 1

        return Fraction(num, din)

    def __floor__(self):

        num = int(math.floor(self.numerator / self.dinominator))
        # num = int(self.numerator / self.dinominator)
        din = 1

        return Fraction(num, din)
