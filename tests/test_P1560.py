import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from P1560 import Solution

class Testing(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test1(self):
        self.assertEqual(self.solution.mostVisited(5, [1, 3, 5]), [1, 2, 3, 4, 5])

if __name__ == "__main__":
    unittest.main()