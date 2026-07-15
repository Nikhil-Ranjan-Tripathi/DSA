class Solution:
    def relativeSort(self, a1, a2):
        order = {}

        # Store first occurrence only
        for i, x in enumerate(a2):
            if x not in order:
                order[x] = i

        a1.sort(key=lambda x: (order.get(x, float('inf')), x))
        return a1