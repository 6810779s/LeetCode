/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function(nums, target) { 
    nums=nums.sort((a,b)=>a-b);
    let result=[]
    for(let i=0;i<nums.length-3;i++){
        if(nums[i]===nums[i-1]) continue;
        for(let j=i+1;j<nums.length-2;j++){
            if(nums[j]===nums[j-1]&&j>i+1) continue;
            let left=j+1;
            let right=nums.length-1;
            while(left<right){
                const sum=nums[i]+nums[j]+nums[left]+nums[right];
                if(sum===target){
                    result.push([nums[i],nums[j],nums[left],nums[right]]);
                    while(nums[right]===nums[right-1]&&right>left) right--;
                    while(nums[left]===nums[left+1]&&right>left) left++;
                    right--;
                    left++;
                    continue;
                }
                if(sum>=target){
                    while(nums[right]===nums[right-1]&&right>left) right--;
                    right--;
                    continue;
                }else{
                    while(nums[left]===nums[left+1]&&right>left) left++;
                    left++;
                    continue;
                }
        }
        }
       
        
      
        
    }
    return result;
};