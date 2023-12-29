class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {num for num in nums2}
        recorring = []
        for num in nums1:
            if num not in recorring and num in hashmap:
                recorring.append(num)
        return recorring
