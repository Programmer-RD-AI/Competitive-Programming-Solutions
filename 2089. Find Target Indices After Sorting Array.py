class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        positions = []
        nums = sorted(nums)
        for idx in range(len(nums)):
            if nums[idx] == target:
                positions.append(idx)
        return positions
