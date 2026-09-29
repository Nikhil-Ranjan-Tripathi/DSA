class Solution:
    def merge(self, inters: list[list[int]]) -> list[list[int]]:
        inters.sort()
        arr = []
        for inter in inters:
            if not arr or inter[0]>arr[-1][1]:
                arr.append(inter)
            else:
                arr[-1][1] = max(arr[-1][1], inter[1])

        return arr


        
