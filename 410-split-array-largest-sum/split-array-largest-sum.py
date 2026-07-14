class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = (left + right) // 2

            groups = 1
            curr = 0

            for num in nums:
                if curr + num > mid:
                    groups += 1
                    curr = num
                else:
                    curr += num

            if groups <= k:
                right = mid
            else:
                left = mid + 1

        return left