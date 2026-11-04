class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = 0
        for i in digits:
            n = n*10+i
        
        n+=1
        n = str(n)
        l = []
        for i in range(len(n)):
            l.append(int(n[i]))

        return l