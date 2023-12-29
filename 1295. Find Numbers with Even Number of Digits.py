class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_no_of_elements = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                even_no_of_elements += 1
        return even_no_of_elements
