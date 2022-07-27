/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    // for (let i=nums.length-1;i>-1;i--){
    //     if(nums[i]===val){
    //         nums.splice(i,1)
    //     }else{
    //         continue;
    //     }
    // }
    let k=0;
    for(let i=0;i<nums.length;i++){
        if(nums[i]===val){
            continue;
        }else{
            if(nums[k]===val){
                nums[k]=nums[i];
                nums[i]=val;
            }else{
                nums[k]=nums[i];
            }
            k++;
        }
    }
    return k;
};