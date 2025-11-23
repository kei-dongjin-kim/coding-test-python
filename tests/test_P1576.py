import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from P1576 import Solution

class TestModifyString(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test1(self):
        result = self.solution.modifyString("j?qg??b")
        self.assertEqual(len(result), 7)
        for i in range(1, len(result)):
            self.assertNotEqual(result[i], result[i-1])

if __name__ == "__main__":
    unittest.main()