from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        for item_arr in arr:
            if item_arr in target:
                target.remove(item_arr)
        return True if target == [] else False
