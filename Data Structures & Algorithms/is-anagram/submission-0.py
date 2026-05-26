class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string = {}
        for w in s:
            if w in string:
                string[w] += 1
            else:
                string[w] = 1
        
        for k in t:
            if k not in string:
                return False
            string[k] -= 1
            if string[k] < 0:
                return False
        
        for n in string.values():
            if n != 0:
                return False
        
        return True