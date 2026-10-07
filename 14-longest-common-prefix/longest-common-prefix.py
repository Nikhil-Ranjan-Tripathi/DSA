class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        a = ''
        for i in range(len(strs[0])):
            a+=strs[0][i]

            for str in strs:
                if str[:i+1]!=a:
                    return a[:len(a)-1]

        return a