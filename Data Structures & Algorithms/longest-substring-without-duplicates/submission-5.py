class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # hash map
        mp = {}
        l = 0
        leng = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            leng = max(leng, r-l+1)
        return leng
        