class Solution:
    def findTwoElement(self, arr):
        arr.sort()

        r = 0
        m = 1

        for i in range(len(arr)):
            if i > 0 and arr[i] == arr[i-1]:
                r = arr[i]

            if arr[i] == m:
                m += 1

        return [r, m]