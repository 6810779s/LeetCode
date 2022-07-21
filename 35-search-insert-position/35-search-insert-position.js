/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    const idx=nums.findIndex(v=>v===target);
    if(idx!==-1){
        return idx;
    }else{
        let left=0;
        let right=nums.length-1;
        while(left<right){
            if(target>nums[left]){
                left++;
            }else if(target<nums[right]){
                right--;
            }
        }
        if(nums[nums.length-1]<target){
            return left+1;
        }
        return left;
    }
};