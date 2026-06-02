class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if not count.get(num, 0):
                count[num] = 1
        max_length = 0
        for k in count:
            if k-1 not in count: # 防止重複訪問，如果前一個在字典裡這個就不會是起點
                length = 0
                while k in count:
                    length += 1
                    k += 1
                max_length = max(length, max_length)
        return max_length
