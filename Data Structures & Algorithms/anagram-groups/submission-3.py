class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for string in strs:
            s = "".join(sorted(string))
            if hashmap.get(s): hashmap[s].append(string)
            else: hashmap[s] = [string]
        
        ans = []
        for key in hashmap:
            ans.append(hashmap[key])
        
        return ans

