class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        new_x = ""
        for idx in range(len(x) - 1, -1, -1):
            new_x += x[idx]
        if x == new_x:
            return True
        return False
