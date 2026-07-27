class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []          # stores indices
        max_area = 0
        n = len(heights)

        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                max_area = max(max_area, h * width)

            stack.append(i)

        while stack:
            h = heights[stack.pop()]

            if stack:
                width = n - stack[-1] - 1
            else:
                width = n

            max_area = max(max_area, h * width)

        return max_area