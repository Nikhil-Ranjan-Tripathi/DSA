class Solution:
    def reverseStack(self, st):
        a = []
        while st:
            a.append(st.pop())
        for i in range(len(a)):
            st.append(a[i])
        