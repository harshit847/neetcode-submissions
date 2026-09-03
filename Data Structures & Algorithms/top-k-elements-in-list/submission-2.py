class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s={}
        for num in nums:
            if num in s:
                s[num]+=1
            else:
                s[num]=1
        freq_dict = sorted(s.items(), key=lambda x:x[1] , reverse=True)
        a=[]
        for i in range(k):
            a.append(freq_dict[i][0])
        return a