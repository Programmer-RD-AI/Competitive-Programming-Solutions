from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        highest = 0
        for account in accounts:
            tot = sum(account)
            if tot > highest:
                highest = tot
        return highest
