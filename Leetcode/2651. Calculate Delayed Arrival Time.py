class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        tot = arrivalTime + delayedTime
        if tot > 24:
            return tot - 24
        elif tot == 24:
            return 0
        else:
            return tot
