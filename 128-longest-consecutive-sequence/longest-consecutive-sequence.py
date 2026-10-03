class Solution:
    def longestConsecutive(self, num: list[int]) -> int:
        if not num:
            return 0
        num.sort()
        l = 1
        temp = 1
        for i in range(1, len(num)):
            if num[i]-num[i-1]==1:
                temp+=1
            elif num[i]==num[i-1]:
                pass
            else:
                temp = 1

            l = max(l, temp)

        return l