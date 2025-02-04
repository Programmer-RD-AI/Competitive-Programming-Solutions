from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result = []
        for idx in range(len(candies)):
            tot = candies[idx] + extraCandies
            result.append(tot >= max_candies)
        return result
