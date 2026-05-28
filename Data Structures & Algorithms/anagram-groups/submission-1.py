class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        matched = set()
        ans = []
        for i in range(len(strs)):
            string = strs[i]
            if i in matched: continue

            group = []
            matched.add(i)
            group.append(string)

            for j in range(i+1, len(strs)):
                comp = strs[j]
                if j in matched: continue

                if self.isAnagram(string, comp):
                    matched.add(j)
                    group.append(comp)
            
            ans.append(group)
        return ans

    def isAnagram(self, s:str, t:str) -> bool:
    
        if len(s) != len(t): return False

        count_s, count_t = {}, {}
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        
        return count_s == count_t
        