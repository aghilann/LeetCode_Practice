import unittest


def romanToInt(s):
    sum = 0

    def value(char):
        if char == "I":
            return 1

        elif char == "V":
            return 5

        elif char == "X":
            return 10

        elif char == "L":
            return 50

        elif char == "C":
            return 100

        elif char == "D":
            return 500

        elif char == "M":
            return 1000

    def greater_then_next(current, current_index):  # Char Current-Index
        if current_index == len(s) - 1:
            return True

        else:
            return value(current) >= value(s[current_index + 1])

    for i, char in enumerate(s):
        if char == "I":
            if greater_then_next(char, i):
                sum += value(char)
            else:
                sum -= value(char)

        elif char == "V":
            if greater_then_next(char, i):
                sum += value(char)
            else:
                sum -= value(char)

        elif char == "X":
            if greater_then_next(char, i):
                sum += value(char)
            else:
                sum -= value(char)

        elif char == "L":
            if greater_then_next(char, i):
                sum += value(char)
            else:
                sum -= value(char)

        elif char == "C":
            if greater_then_next(char, i):
                sum += value(char)
            else:
                sum -= value(char)

        elif char == "D":
            if greater_then_next(char, i):
                sum += value(char)
            else:
                sum -= value(char)

        elif char == "M":
            if greater_then_next(char, i):
                sum += value(char)
            else:
                sum -= value(char)

    return sum


class Test(unittest.TestCase):

    def test_romanToInt(self):
        self.assertEqual(romanToInt("III"), 3)
        self.assertEqual(romanToInt("XXX"), 30)
        self.assertEqual(romanToInt("LVIII"), 58)
        self.assertEqual(romanToInt("IV"), 4)
        self.assertEqual(romanToInt("DM"), 500)
        self.assertEqual(romanToInt("MCMXCIV"), 1994)


if __name__ == "__main__":
    unittest.main()
