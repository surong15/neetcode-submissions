class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[i, 0] for i in range(-1000, 1001)]
        for num in nums:
            count[num+1000][1] += 1
        count.sort(key = lambda x: x[1], reverse=True)
        ans = []
        for i in range(k):
            ans.append(count[i][0])
        return ans



