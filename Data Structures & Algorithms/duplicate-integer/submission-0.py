class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        val = None
        for x in nums:
            if x == val: return True
            val = x
        return False