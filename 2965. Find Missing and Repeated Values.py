import random


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        all_values = []
        repeated = []
        for row in grid:
            all_values.extend(row)
        possibiltities = [x + 1 for x in range(max(all_values) + 1)]
        for val in all_values:
            if val in possibiltities:
                possibiltities.remove(val)
            if type(repeated) is list:
                if val in repeated:
                    repeated = val
                else:
                    repeated.append(val)
        possibiltities.append(-1)
        return [repeated, possibiltities[0]]
