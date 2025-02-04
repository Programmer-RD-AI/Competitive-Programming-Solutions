from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_nos = []
        negative_nos = []
        mixed_nums = []
        for num in nums:
            if num > 0:
                positive_nos.append(num)
            else:
                negative_nos.append(num)
        for idx in range(len(positive_nos)):
            mixed_nums.append(positive_nos[idx])
            mixed_nums.append(negative_nos[idx])
        return mixed_nums
