/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    const nums = nums1.concat(nums2).sort((a,b)=>a-b)

    return nums.length%2===0?(nums[(nums.length/2)-1]+nums[nums.length/2])/2:nums[Math.floor(nums.length/2)]
};