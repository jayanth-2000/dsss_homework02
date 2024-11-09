import unittest
from math_quiz import get_integer, get_random_operator, get_expression


class TestMathQuizFunctions(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random integers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = get_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val, "Random integer out of bounds")

    def test_generate_random_operator(self):
        # Test if generated operator is one of the allowed operators
        allowed_operators = ['+', '-', '*']
        for _ in range(100):  # Test multiple times for randomness
            operator = get_random_operator()
            self.assertIn(operator, allowed_operators, "Generated operator is not among '+', '-', '*'")

    def test_calculate_expression(self):
        # Define test cases for get_expression function
        test_cases = [
            (5, 2, '+', '5 + 2', 3),  # Intentional "incorrect" answer logic
            (7, 3, '-', '7 - 3', 10),  # Intentional "incorrect" answer logic
            (4, 2, '*', '4 * 2', 8)    # Multiplication answer should be correct
        ]

        # Test each case to see if the problem and answer are as expected
        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = get_expression(num1, num2, operator)
            self.assertEqual(problem, expected_problem, "Problem string mismatch")
            self.assertEqual(answer, expected_answer, "Incorrect calculated answer")

if __name__ == "__main__":
    unittest.main()

