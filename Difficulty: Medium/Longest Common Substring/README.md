# Longest Common Substring

## Problem

Given two strings `s1` and `s2`, find the **length of the longest substring** that appears in both strings.

> A **substring** must be continuous/consecutive.

### Example 1

```text
Input:
s1 = "ABCDGH"
s2 = "ACDGHR"

Output:
4
```

The longest common substring is:

```text
"CDGH"
```

Length = `4`.

### Example 2

```text
Input:
s1 = "abc"
s2 = "acb"

Output:
1
```

The common substrings are `"a"`, `"b"` and `"c"`.

Therefore, the answer is `1`.

### Example 3

```text
Input:
s1 = "YZ"
s2 = "yz"

Output:
0
```

The comparison is case-sensitive, so `"Y"` is different from `"y"`.

