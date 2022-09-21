class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer=[]
        num_sum=0
        dic={}
        for num,i in enumerate(nums):
            dic[num]=i
            if i%2==0:
                num_sum+=i
        for i in queries:
            val = i[0]
            idx = i[1]
            num_idx = dic[idx]+val
            if dic[idx]%2==0:
                num_sum-=dic[idx]
            
            if num_idx%2==0:
                num_sum+=num_idx
            
            dic[idx] = num_idx
            answer.append(num_sum)
            
        
        return answer
    