class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        all_elements = []
        count = 0
        for row in grid:
            all_elements.extend(row)
        for element in all_elements:
            if element < 0:
                count += 1
        return count
