from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        tot = 0
        for idx in range(len(operations)):
            tot += 1 if "+" in operations[idx] else -1
        return tot
