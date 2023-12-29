class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        occurs = {}
        for num in nums:
            if num not in occurs.keys():
                occurs[num] = 1
            else:
                occurs[num] += 1
        for num, occurences in zip(occurs.keys(), occurs.values()):
            if occurences == 1:
                return num
        return 0
