class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        cnt = 0
        keyword = word
        while keyword in sequence:
            keyword += word
            cnt += 1
        return cnt

        # l = len(sequence)
        # m = len(word)
        # if l == m and sequence == word:
        #     return 1
        # max_val = 0
        # for i in range(l - m + 1):
        #     curr = 0
        #     while i < l - m + 1:
        #         if word == sequence[i:i + m]:
        #             i += m
        #             curr += 1
        #             max_val = max(max_val, curr)
        #         else:
        #             i += 1
        #             curr = 0
        # return max_val
