class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_leng = 0

        for num in s:
            if num-1 not in s:
                leng = 1
                while num+leng in s:
                    leng += 1
                max_leng = max(leng, max_leng)
        return max_leng