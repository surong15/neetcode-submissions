class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # hash set
        charSet = set()
        l = 0
        leng = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            leng = max(leng, r-l+1)
        return leng