const threeSum = function(nums) {
    let answer =[];
    nums=nums.sort((a,b)=>a-b);
    for(let i=0;i<nums.length-2;i++){
        if(nums[i]===nums[i-1]) continue;
        let left=i+1;
        let right=nums.length-1;
        while(left<right){
            const sum=nums[i]+nums[left]+nums[right];
            if(sum===0){
                answer.push([nums[i],nums[left],nums[right]]);
                while(nums[right]===nums[right-1]&&right>left) right--;
                while(nums[left]===nums[left+1]&&right>left) left++;
                right--;
                left++;
                continue;
            }
           
            if(sum>0){
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
    return answer
};