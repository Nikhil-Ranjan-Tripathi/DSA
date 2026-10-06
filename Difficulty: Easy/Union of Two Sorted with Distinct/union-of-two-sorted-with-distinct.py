class Solution:
    def findUnion(self, a, b):
        i = 0
        j = 0
        ans = []

        while i < len(a) and j < len(b):

            if a[i] < b[j]:
                ans.append(a[i])
                i += 1

            elif a[i] > b[j]:
                ans.append(b[j])
                j += 1

            else:
                ans.append(a[i])
                i += 1
                j += 1

        while i < len(a):
            ans.append(a[i])
            i += 1

        while j < len(b):
            ans.append(b[j])
            j += 1

        return ans