class Solution:
    def subarraySum(self, arr, target):
        s = 0
        i = 0

        for j in range(len(arr)):

            s += arr[j]

            while s > target and i <= j:
                s -= arr[i]
                i += 1

            if s == target:
                return [i + 1, j + 1]

        return [-1]