from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        existed = set()
        for num in nums:
            if num not in existed:
                existed.add(num)
            else:
                return True
        return None
