from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        l = len(boxes)
        answer = [0] * l
        for i in range(l):
            sum_ = 0
            for j in range(l):
                if boxes[j] == "1":
                    sum_ += abs(i - j)
            answer[i] = sum_
        return answer