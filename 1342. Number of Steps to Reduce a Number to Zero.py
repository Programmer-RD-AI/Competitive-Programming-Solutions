class Solution:
    def numberOfSteps(self, num: int) -> int:
        if 0 > num and num > 106:
            return 0
        count = 0
        while num != 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            count += 1
        return count
