import unittest
import sys
import os

curr_dir = os.path.dirname(__name__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P0401 import Solution

class TestP0401(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()

  def test1(self):
    self.assertEqual(self.solution.readBinaryWatch(8), ['7:31', '7:47', '7:55', '7:59', '11:31', '11:47', '11:55', '11:59'])

if __name__ == "__main__":
  unittest.main()