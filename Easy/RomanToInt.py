import unittest


def romanToInt(s):
    sum = 0
    
    letter_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
    def value(char):
        return letter_values[char]

    def greater_then_next(current, current_index):  # Char Current-Index
        if current_index == len(s) - 1:
            return True

        else:
            return value(current) >= value(s[current_index + 1])

    for i, char in enumerate(s):
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
