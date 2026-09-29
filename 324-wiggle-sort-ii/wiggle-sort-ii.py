class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        nums.sort()
        if len(nums)%2==1:
            a = nums[:len(nums)//2+1]
            b = nums[len(nums)//2+1:]
        else:
            a = nums[:len(nums)//2]
            b = nums[len(nums)//2:]
        a = a[::-1]
        b = b[::-1]
        for i in range(len(nums)):
            if i%2==0:
                nums[i] = a[0]
                a.pop(0)
            else:
                if b:
                    nums[i] = b[0]
                    b.pop(0)

        return nums
