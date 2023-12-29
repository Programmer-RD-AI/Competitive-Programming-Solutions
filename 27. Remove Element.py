class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 1
        new_nums = nums.copy()
        for idx in range(len(new_nums)):
            if new_nums[idx] != val:
                count += 1
            else:
                nums.pop(nums.index(new_nums[idx]))
        return count
