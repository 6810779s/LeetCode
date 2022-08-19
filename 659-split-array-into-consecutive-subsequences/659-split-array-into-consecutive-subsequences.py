class Solution(object):
    def isPossible(self, nums):
        count=Counter(nums)
        prev_dict=defaultdict(int)
        for i in nums:
            print("i:",i)
            if count[i]==0:
                continue
            elif prev_dict[i-1]>0 :
                prev_dict[i-1]-=1
                prev_dict[i]+=1
                count[i]-=1
            elif count[i]>0 and count[i+1]>0 and count[i+2]>0:
                count[i]-=1
                count[i+1]-=1
                count[i+2]-=1
                prev_dict[i+2]+=1
            else:
                return False
        return True