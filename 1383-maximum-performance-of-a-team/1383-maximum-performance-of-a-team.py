class Solution:
     def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        # sort in descending order of efficiency and make an array with efficiency and speed tuple as an element
        engineer_eff_speed = sorted(zip(efficiency, speed), reverse = True)
        
        # min heap is to pop the engineer with least speed after heap length becomes k but one more engineer is to be added
        min_heap = [] 
        
        # total speed is used to calculate the final performance of all engineers assembled for max performance
        speed = 0
        
        # total performance is speed + minimum efficiency
        performance = 0
        
        for i in range(len(engineer_eff_speed)):
            
            
            eff_of_eng = engineer_eff_speed[i][0]
            
            speed_of_eng = engineer_eff_speed[i][1]
            
            # only k elements can be there in heap 
            if(len(min_heap) == k):
                speed -= heappop(min_heap)
            
            heappush(min_heap, speed_of_eng)
            
            speed += speed_of_eng
            
            performance = max(performance, speed * eff_of_eng)
            
        return performance % (10**9+7)
        