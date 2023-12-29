class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        divisible = 0
        non_divisible = 0
        for i in range(1, n + 1):
            if i % m == 0:
                divisible += i
            else:
                non_divisible += i
        return non_divisible - divisible
