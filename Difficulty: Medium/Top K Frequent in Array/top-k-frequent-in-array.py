class Solution:
    def topKFreq(self, arr, k):

        c = {}

        for x in arr:
            c[x] = c.get(x, 0) + 1

        a = sorted(c.items(), key=lambda x: (x[1], x[0]), reverse=True)

        result = []

        for key, value in a[:k]:
            result.append(key)

        return result