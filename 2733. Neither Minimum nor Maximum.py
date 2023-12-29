class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return -1
        maximum = max(nums)
        minimum = min(nums)
        nums.remove(maximum)
        nums.remove(minimum)
        if len(nums) >= 1:
            return nums[0]
        return -1
