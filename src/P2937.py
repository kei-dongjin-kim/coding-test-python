class Solution:
  def findMinimumOperations(s1: str, s2: str, s3: str) -> int:
    if s1[0] != s2[0] or s2[0] != s3[0]:
        return -1

    curr = 0
    min_len = min(len(s1), len(s2), len(s3))

    while curr < min_len:
        if s1[curr] != s2[curr] or s2[curr] != s3[curr]:
            break
        curr += 1

    return (len(s1) - curr) + (len(s2) - curr) + (len(s3) - curr)