class Solution:
    def isSorted(self, arr) -> bool:
        a = sorted(arr)
        return arr==a