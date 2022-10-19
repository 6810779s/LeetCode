class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic={}
        for word in words:
            if word in dic:
                dic[word]+=1
            else:
                dic[word]=1
        
        
        dic_sort=sorted(dic.items(),key=lambda x:(-x[1],x[0]))
        arr=[]
        for i in range(k):
            arr.append(dic_sort[i][0])
        return arr
        