/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let idx=0;
    while(idx!==nums.length){
            if(nums[idx-1]===nums[idx]){
                nums.splice(idx,1)
                continue;
            }else{
                idx++;
            }
         }
};