from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            if num not in hashmap.keys():
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        hash_vals = list(hashmap.values())
        hash_keys = list(hashmap.keys())
        return hash_keys[hash_vals.index(max(hash_vals))]
