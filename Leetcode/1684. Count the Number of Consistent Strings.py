from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = list(allowed)
        count = 0
        for word in words:
            word = list(word)
            if all(element in allowed for element in word):
                count += 1
        return count
