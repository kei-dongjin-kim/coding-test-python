import unittest
import sys
import os

# src 디렉토리 경로를 import 경로에 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from P1854 import Solution  # Solution 클래스가 정의된 파일 이름에 맞춰 import

class TestMaximumPopulation(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        logs = [[1950, 1961], [1960, 1971], [1970, 1981]]
        self.assertEqual(self.solution.maximumPopulation(logs), 1960)

if __name__ == "__main__":
    unittest.main()