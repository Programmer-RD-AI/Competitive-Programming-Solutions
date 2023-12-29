class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        tracker = 0
        tot = 0
        while tracker < n:
            tot = tot ^ start
            tracker += 1
            start += 2
            print(tot, start, tracker)
        return tot
