from itertools import permutations
class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        arr = []
        for p in permutations(nums):
            if list(p) not in arr:
                arr.append(list(p))

        return arr