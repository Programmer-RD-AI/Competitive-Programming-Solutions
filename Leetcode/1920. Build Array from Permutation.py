from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        new_array = []
        for idx in range(len(nums)):
            new_array.append(nums[nums[idx]])
        return new_array
