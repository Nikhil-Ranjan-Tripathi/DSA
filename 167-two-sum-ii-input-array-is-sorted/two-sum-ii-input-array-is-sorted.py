class Solution(object):
    def twoSum(self, numbers, target):
        s = {}

        for i in range(len(numbers)):
            a = target - numbers[i]
            if a in s:
                return s[a]+1, i+1

            s[numbers[i]] = i            

