import unittest
import sys
import os

curr_dir = os.path.dirname(__name__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P3798 import Solution

class TestP3798(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.largestEven("221221221"), "22122122")

if __name__ == "__main__":
  unittest.main()
