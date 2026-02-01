import unittest
import sys
import os
from UserDefinedDataType import ListNode

curr_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P2807 import Solution

class TestP2807(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()
  
  def test1(self):
    self.assertEqual(self.solution.insertGreatestCommonDivisors(ListNode.from_list([1, 2, 4, 8, 16])), ListNode.from_list([1, 1, 2, 2, 4,4, 8, 8, 16]))

if __name__ == "__main__":
  unittest.main()
