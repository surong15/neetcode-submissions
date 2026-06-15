class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]

        mid = len(nums)//2
        if nums[mid] > nums[0]:
            return self.findMin(nums[mid:])
        else:
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            else:
                return self.findMin(nums[:mid])