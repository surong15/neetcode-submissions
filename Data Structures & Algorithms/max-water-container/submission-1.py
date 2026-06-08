class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # sliding window
        res = 0
        for w in range(1, len(heights)):
            i = 0
            while i+w < len(heights):
                h = min(heights[i], heights[i+w])
                res = max(res, w*h)
                i += 1
        return res
        