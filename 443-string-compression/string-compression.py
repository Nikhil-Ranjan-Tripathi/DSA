from collections import Counter
class Solution:
    def compress(self, chars: list[str]) -> int:
        # i = 0
        # write = 0

        # while i < len(chars):
        #     ch = chars[i]
        #     j = i

        #     while j < len(chars) and chars[j] == ch:
        #         j += 1

        #     count = j - i

        #     # Write the character
        #     chars[write] = ch
        #     write += 1

        #     if count > 1:
        #         for digit in str(count):
        #             chars[write] = digit
        #             write += 1

        #     i = j

        # return write


        stri = []
        stri.append(chars[0])
        c = 1
        for i in range(1, len(chars)):
            if chars[i] == chars[i-1]:
                c+=1
            else:
                if c!=1:
                    l = list(str(c))
                    stri+=l
                stri.append(chars[i])
                c = 1
        if c!=1:
            l = list(str(c))
            stri+=l

        for i in range(len(chars)):
            chars.pop(0)

        for i in stri:
            chars.append(i)
        
                
        

