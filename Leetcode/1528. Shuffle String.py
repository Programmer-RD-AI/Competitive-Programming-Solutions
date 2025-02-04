from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new_string = [None] * len(s)
        for idx, indi_idx in enumerate(indices):
            new_string[indi_idx] = s[idx]
        print(new_string)
        return "".join(new_string)
