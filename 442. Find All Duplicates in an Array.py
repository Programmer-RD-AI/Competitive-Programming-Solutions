class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if 1 > n and n > 10**5:
            return 0
        occurening_numbers = {}
        recorrecing = []
        for num in nums:
            if num not in occurening_numbers.keys():
                occurening_numbers[num] = 1
            else:
                occurening_numbers[num] += 1
        for num, no_of_occurences in zip(
            occurening_numbers.keys(), occurening_numbers.values()
        ):
            if no_of_occurences > 1:
                recorrecing.append(num)
        return recorrecing
