from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx in range(len(nums)):
            num = nums[idx]
            diff = target - num
            if diff in hashmap.keys():
                return [hashmap[diff], idx]
            hashmap[num] = idx
