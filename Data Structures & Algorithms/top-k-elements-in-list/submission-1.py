class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        res = dict(sorted(count.items(), key = lambda x: x[1], reverse=True))
        ans = []
        for item in res:
            if k != 0:
                ans.append(item)
                k -= 1
        
        return ans
