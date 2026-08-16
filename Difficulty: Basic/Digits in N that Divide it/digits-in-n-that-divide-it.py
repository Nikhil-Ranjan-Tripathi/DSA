class Solution:
    def divisibleByDigits(self, s):
        rem = [0] * 10

        for ch in s:
            digit = int(ch)

            for d in range(1, 10):
                rem[d] = (rem[d] * 10 + digit) % d

        count = 0

        for ch in s:
            digit = int(ch)

            if digit != 0 and rem[digit] == 0:
                count += 1

        return count