from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if 1 > n and n > 10**5:
            return 0
        occurring_numbers = {}
        re_correcting = []
        for num in nums:
            if num not in occurring_numbers.keys():
                occurring_numbers[num] = 1
            else:
                occurring_numbers[num] += 1
        for num, no_of_occurrences in zip(
            occurring_numbers.keys(), occurring_numbers.values()
        ):
            if no_of_occurrences > 1:
                re_correcting.append(num)
        return re_correcting
