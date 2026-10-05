class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        arr = []
        intervals.append(newInterval)
        intervals.sort()

        for inter in intervals:
            if not arr or inter[0]>arr[-1][1]:
                arr.append(inter)
            else:
                arr[-1][1] = max(inter[1], arr[-1][1])

        return arr