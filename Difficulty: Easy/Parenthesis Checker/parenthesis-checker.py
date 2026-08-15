class Solution:
    def isBalanced(self, s):
        # code here
        d = {")":"(", "}": "{", "]": "["}
        a = []
        for i in s:
            if i in '({[':
                a.append(i)
            else:
                if not a:
                    return False
                if a[-1]==d[i]:
                    a.pop()
                else:
                    return False
                
            
        if len(a)==0:
            return True
        else:
            return False
                