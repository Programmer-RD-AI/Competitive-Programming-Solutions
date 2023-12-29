class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        differences = []
        arr = sorted(arr)
        for i in range(1, len(arr)):
            diff = arr[i - 1] - arr[i]
            differences.append(diff)
        return differences.count(differences[0]) == len(differences)
