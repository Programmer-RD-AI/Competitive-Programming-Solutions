class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        sorted_heights = sorted(heights.copy())
        sorted_heights.reverse()
        sorted_names = []
        for sh in sorted_heights:
            sorted_names.append(names[heights.index(sh)])
        return sorted_names
