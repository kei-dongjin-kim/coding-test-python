import unittest
import sys
import os

curr_dir = os.path.dirname(__name__)
src_dir = os.path.abspath(os.path.join(curr_dir, "..", "src"))
sys.path.append(src_dir)

from P0551 import Solution

class TestP0551(unittest.TestCase):

  def setUp(self):
    self.solution = Solution()
  
  def test1(self):
    self.assertFalse(self.solution.checkRecord("PPPAPPPPPPPLLLPPPPPPPPP"))

if __name__ == "__main__":
  unittest.main()
