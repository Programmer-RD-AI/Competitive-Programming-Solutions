from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new_nums = []
        for x_nums, y_nums in zip(nums[:n], nums[n:]):
            new_nums.append(x_nums)
            new_nums.append(y_nums)
        return new_nums
