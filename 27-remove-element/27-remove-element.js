/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    for (let i=nums.length-1;i>-1;i--){
        if(nums[i]===val){
            nums.splice(i,1)
        }else{
            continue;
        }
    }
};