/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
   const nums_length=nums1.length+nums2.length;
    const nums = nums1.concat(nums2).sort((a,b)=>a-b)

    return nums_length%2===0?(nums[(nums.length/2)-1]+nums[nums.length/2])/2:nums[Math.floor(nums.length/2)]
};