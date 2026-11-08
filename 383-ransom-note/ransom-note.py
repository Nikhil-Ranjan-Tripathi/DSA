from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1 = Counter(ransomNote)
        c2 = Counter(magazine)

        for k, v in c1.items():
            if k not in c2:
                return False
            else:
                if v>c2[k]:
                    return False

        return True


"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote)>len(magazine):
            return False
        for c in set(ransomNote):
            if magazine.count(c)<ransomNote.count(c):
                return False

        return True

# Python's count() counts how many times a character appears in a string.

# magazine = "aabbbc"
# ransomNote = "aabb"

# magazine.count('a')     # 2
# ransomNote.count('a')   # 1

# magazine.count('b')     # 3
# ransomNote.count('b')   # 2
"""
