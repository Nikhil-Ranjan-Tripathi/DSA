class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        l = [""]*numRows

        currentRow = 0
        direction = 1

        for char in s:

            l[currentRow] += char

            if currentRow==0:
                direction = 1
            elif currentRow == len(l)-1:
                direction = -1

            currentRow+=direction

        return "".join(l)