from collections import Counter

class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        freq_char = Counter(s)
        freq_val = Counter(freq_char.values())
        max_cnt = max(freq_val.values())
        max_freq = -1
        for key, val in freq_val.items():
            if val == max_cnt:
                if key > max_freq:
                    max_freq = key
        res = ''
        for key, val in freq_char.items():
            if val == max_freq:
                res += key
        return res