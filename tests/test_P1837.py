import unittest
import sys
import os

curr_dir = os.path.dirname(__name__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P1837 import Solution

class Test1837(unittest.TestCase):
  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.sumBase(123, 5), 11)

if __name__ == "__main__":
  unittest.main()