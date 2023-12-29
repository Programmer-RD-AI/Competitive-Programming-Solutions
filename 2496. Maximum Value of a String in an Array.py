class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        strs_lengths = []
        for string in strs:
            if string.isnumeric():
                strs_lengths.append(int(string))
            else:
                strs_lengths.append(len(string))
        return max(strs_lengths)
