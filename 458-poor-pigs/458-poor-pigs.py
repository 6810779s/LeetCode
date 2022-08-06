class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        times=minutesToTest/minutesToDie
        pigs=0
        
        while((times+1)**pigs<buckets):
            print((times+1)**pigs)
            pigs+=1
        
        return pigs
            
        