class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l < r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            if nums[r] == target:
                return r
            if nums[l] == target:
                return l

            if nums[m] > nums[l]:
                if nums[l] <= target and target < nums[m]:
                    r = m
                else:
                    l = m+1
            else:
                if nums[m] < target and target < nums[l]:
                    l = m+1
                else:
                    r = m

        if l == r and nums[l] == target:
            return l

        return -1