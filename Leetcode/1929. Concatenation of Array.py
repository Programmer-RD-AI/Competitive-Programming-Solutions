from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        for idx in range(len(nums)):
            nums.append(nums[idx])
        # nums.extend(nums)
        return nums
