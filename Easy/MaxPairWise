import unittest

def max_pairwise_product(numbers):
    highest = 0
    second_highest = 0

    for n in numbers:
        if n >= highest:
            second_highest = highest
            highest = n
        elif n >= second_highest:
            second_highest = n
    
    return highest * second_highest

class Test(unittest.TestCase):

    def test_add(self):
        self.assertEqual(max_pairwise_product([1, 2, 3, 8, 4, 5, 20]), 160)
        self.assertEqual(max_pairwise_product([1, 2, 3, 15, 4, 5, 10]), 150)
        self.assertEqual(max_pairwise_product([1, 3, 3, 1]), 9)
        self.assertEqual(max_pairwise_product([3, 3, 3, 3]), 9)


if __name__ == "__main__":
    unittest.main()
