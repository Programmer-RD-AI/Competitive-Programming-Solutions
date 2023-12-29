class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            count = 0
            for n in nums:
                if num > n:
                    count += 1
            result.append(count)
        return result
