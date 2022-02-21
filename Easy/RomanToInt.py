import unittest


def romanToInt(s):
    sum = 0
        i = 0
        letters = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        stop = (len(s) - 1) # One before final
        
        while i < stop:
            if letters[s[i]] < letters[s[i+1]]:
                sum -= letters[s[i]]
            else:
                sum += letters[s[i]]
            i += 1
        sum += letters[s[-1]]
        
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
