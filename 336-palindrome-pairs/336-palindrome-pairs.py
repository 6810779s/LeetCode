class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        rmap = {w[::-1]:i for i,w in enumerate(words)}
        res = []
        
        for i,w in enumerate(words):
            if w in rmap:
                if rmap[w] != i:
                    res.append([i,rmap[w]])
            for j in range(1,len(w)+1):
                # print("rmap:",rmap)
                # print("w:",w)
                # print("i:",i,"j:",j)
                # print("w[:-j]:",w[:-j],"w[-j:][::-1]:",w[-j:][::-1])
                # print("w[-j:]:",w[-j:])
                # print("w[j:]:",w[j:]," w[:j][::-1]:", w[:j][::-1])
                # print("w[:j]:",w[:j])
                if w[:-j] in rmap and w[-j:] == w[-j:][::-1]:
                        # print("1111111111111111111111")
                        res.append([i,rmap[w[:-j]]])
                if w[j:] in rmap and w[:j] == w[:j][::-1]:
                    # print("2222222222222222222222")
                    res.append([rmap[w[j:]],i])
        return res