from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        tot = 0
        for idx in range(len(nums)):
            tot += nums[idx]
            nums[idx] = tot
        return nums
