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

---

## Important: Substring vs Subsequence

This is the most important concept in this problem.

### Substring

Characters must be **next to each other**.

```text
"ABCDEF"
   ↑↑↑
   CDE
```

`CDE` is a substring.

### Subsequence

Characters don't have to be next to each other.

```text
"ABCDEF"
 ↑  ↑ ↑
 A  C F
```

`ACF` is a subsequence.

Therefore:

```text
Longest Common Substring != Longest Common Subsequence
```

---

# Approach 1: Brute Force

We can generate substrings and check whether they exist in the other string.

For example:

```text
s1 = "abcd"
```

Possible substrings include:

```text
a
ab
abc
abcd
b
bc
bcd
c
cd
d
```

Then check which of them occur in `s2`.

However, this approach can become expensive because we generate many substrings and perform searches.

So Dynamic Programming is the better approach for this problem.

---

# Approach 2: Dynamic Programming

## Main Idea

We compare every character of `s1` with every character of `s2`.

The key question is:

> If `s1[i-1] == s2[j-1]`, how long is the common substring ending at these two characters?

If the characters match:

```text
dp[i][j] = dp[i-1][j-1] + 1
```

If they don't match:

```text
dp[i][j] = 0
```

The `0` is extremely important.

Why?

Because a substring must be **continuous**.

When characters don't match, the current continuous substring is broken.

---

# DP Definition

We create a 2D array:

```text
dp[i][j]
```

Meaning:

> `dp[i][j]` = length of the longest common substring that **ends at** `s1[i-1]` and `s2[j-1]`.

We use `i-1` and `j-1` because our DP table has an extra first row and column.

---

# DP Transition

### Case 1: Characters match

If:

```text
s1[i-1] == s2[j-1]
```

then:

```text
dp[i][j] = dp[i-1][j-1] + 1
```

We extend the previous common substring.

### Case 2: Characters don't match

If:

```text
s1[i-1] != s2[j-1]
```

then:

```text
dp[i][j] = 0
```

The continuous substring has been broken.

---

# Why do we use `dp[i-1][j-1]`?

Suppose:

```text
s1 = "ABCD"
s2 = "XBCD"
```

When comparing:

```text
D == D
```

we look diagonally backwards:

```text
C == C
```

then:

```text
B == B
```

then:

```text
```

So the common substring grows diagonally:

```text
B
BC
BCD
```

That's why the transition is:

```text
dp[i][j] = dp[i-1][j-1] + 1
```

---

# DP Table Example

Consider:

```text
s1 = "ABC"
s2 = "XBC"
```

We create:

```text
      ""  X  B  C
 ""    0  0  0  0
 A     0  0  0  0
 B     0  0  1  0
 C     0  0  0  2
```

Let's trace it.

### Compare `A` with `X`

```text
A != X
```

Therefore:

```text
dp[1][1] = 0
```

### Compare `B` with `B`

```text
B == B
```

Therefore:

```text
dp[2][2] = dp[1][1] + 1
         = 0 + 1
         = 1
```

### Compare `C` with `C`

```text
C == C
```

Therefore:

```text
dp[3][3] = dp[2][2] + 1
         = 1 + 1
         = 2
```

So:

```text
BC
```

has length `2`.

---

# Why don't we take the maximum from the previous cells?

This is a common confusion.

For **Longest Common Subsequence**, we often do:

```text
dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

But for **Longest Common Substring**, we don't do that.

We do:

```text
if s1[i-1] == s2[j-1]:
    dp[i][j] = dp[i-1][j-1] + 1
else:
    dp[i][j] = 0
```

Because substring means **continuous**.

---

# Python Solution

```python
class Solution:
    def longCommSubstr(self, s1, s2):
        n = len(s1)
        m = len(s2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        ans = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):

                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    ans = max(ans, dp[i][j])

                else:
                    dp[i][j] = 0

        return ans
```

---

# Step-by-Step Code

### Step 1: Get lengths

```python
n = len(s1)
m = len(s2)
```

---

### Step 2: Create DP table

```python
dp = [[0] * (m + 1) for _ in range(n + 1)]
```

Why `n + 1` and `m + 1`?

Because we keep an extra row and column for the empty string.

For example:

```text
       ""  X  B  C
""      0  0  0  0
A       0  0  0  0
B       0  0  0  0
C       0  0  0  0
```

---

### Step 3: Compare every pair of characters

```python
for i in range(1, n + 1):
    for j in range(1, m + 1):
```

We compare:

```python
s1[i - 1]
```

with:

```python
s2[j - 1]
```

---

### Step 4: If they match

```python
if s1[i - 1] == s2[j - 1]:
    dp[i][j] = dp[i - 1][j - 1] + 1
```

We extend the previous substring.

---

### Step 5: If they don't match

```python
else:
    dp[i][j] = 0
```

The continuous sequence has been broken.

---

### Step 6: Keep the largest value

```python
ans = max(ans, dp[i][j])
```

Unlike some DP problems, the answer isn't necessarily stored in:

```text
dp[n][m]
```

Instead, the answer can occur anywhere in the table.

So we maintain:

```python
ans
```

---

# Complexity

Let:

```text
n = len(s1)
m = len(s2)
```

### Time Complexity

We compare every character of `s1` with every character of `s2`.

```text
O(n × m)
```

### Space Complexity

The 2D DP table contains:

```text
(n + 1) × (m + 1)
```

elements.

Therefore:

```text
O(n × m)
```

The current GFG problem lists `O(n*m)` time and `O(n*m)` auxiliary space for the expected DP solution.

---

# Space Optimized DP

Notice that:

```python
dp[i][j] = dp[i - 1][j - 1] + 1
```

Only the **previous row** is required.

Therefore, we can reduce the space from:

```text
O(n × m)
```

to:

```text
O(m)
```

```python
class Solution:
    def longCommSubstr(self, s1, s2):
        n = len(s1)
        m = len(s2)

        prev = [0] * (m + 1)

        ans = 0

        for i in range(1, n + 1):

            curr = [0] * (m + 1)

            for j in range(1, m + 1):

                if s1[i - 1] == s2[j - 1]:
                    curr[j] = prev[j - 1] + 1
                    ans = max(ans, curr[j])

            prev = curr

        return ans
```

Complexity:

```text
Time  = O(n × m)
Space = O(m)
```

GFG also describes this space-optimization idea: because the current value depends on the previous row's diagonal value, only consecutive rows need to be maintained.

---

# Pattern to Remember

This problem belongs to:

```text
Dynamic Programming
        ↓
String DP
        ↓
Compare two strings
        ↓
Longest Common Substring
```

The most important template is:

```python
if s1[i - 1] == s2[j - 1]:
    dp[i][j] = dp[i - 1][j - 1] + 1
else:
    dp[i][j] = 0
```

And remember:

```text
SUBSTRING
    ↓
continuous
    ↓
mismatch → 0
```

Whereas:

```text
SUBSEQUENCE
    ↓
not necessarily continuous
    ↓
usually involves max(left, up)
```

---

# Common Mistake

A brute-force solution such as:

```python
for i in range(len(s1)):
    for j in range(i, len(s1)):
        if s1[i:j+1] in s2:
            ans = max(ans, j - i + 1)
```

can work for some inputs, but it is not the intended `O(n*m)` DP solution and can become expensive because substring creation/search adds additional work.

The DP solution directly compares character pairs and builds the answer from smaller subproblems.

---

# Related Problems

Once you understand this problem, study these next:

1. Longest Common Subsequence
2. Longest Repeated Subsequence
3. Shortest Common Supersequence
4. Edit Distance
5. Longest Palindromic Subsequence
6. Longest Palindromic Substring

These are all useful **String DP** patterns. GFG's DP problem lists group Longest Common Substring with several of these string-DP problems.

---

# Key Takeaway

For **Longest Common Substring**:

```text
Characters match
        ↓
take diagonal + 1

Characters don't match
        ↓
reset to 0

Every cell
        ↓
update global maximum
```

The one line to remember is:

```python
dp[i][j] = dp[i - 1][j - 1] + 1
```

and on mismatch:

```python
dp[i][j] = 0
```

### GFG

[Longest Common Substring — GFG](https://www.geeksforgeeks.org/problems/longest-common-substring1452/1)
