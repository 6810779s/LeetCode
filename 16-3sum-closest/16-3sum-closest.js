/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
    nums=nums.sort((a,b)=>a-b);
    let answer=Infinity;
    for(let i=0;i<nums.length-2;i++){
        let left=i+1;
        let right=nums.length-1;
        while(left<right){
            const sum = nums[i]+nums[left]+nums[right];
            if(Math.abs(sum-target)<Math.abs(answer-target)) answer=sum;
            if(sum>target){
                right--;
            }else{
                left++;
            }
        } 
    }
    return answer;
};