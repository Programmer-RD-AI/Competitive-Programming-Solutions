class Solution:
    def reverse(self, x: int) -> int:
        new_x = ""
        x = str(x)
        for x_idx in range(len(x) - 1, -1, -1):
            new_x += x[x_idx]
        try:
            new_x = int(new_x)
        except Exception as _:
            position = len(new_x) - 1
            new_x = -int(new_x[:position])
        print(new_x, -(2**31) <= new_x, new_x <= 2**31 - 1)
        if -(2**31) <= new_x and new_x <= 2**31 - 1:
            return new_x
        return 0
