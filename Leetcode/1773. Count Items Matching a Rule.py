from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ruleDict = {"type": 0, "color": 1, "name": 2}
        ruleId = ruleDict[ruleKey]
        count = 0
        for item in items:
            if item[ruleId] == ruleValue:
                count += 1
        return count
