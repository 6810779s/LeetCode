var maxArea = function(height) {
    let left=0;
    let right = height.length-1;
    let max_width=0;
    while(left<right){
        let cur_height;
        let width = right-left;
        if(height[left]>height[right]){
            cur_height=height[right];
            right--;
        }else{
            cur_height=height[left];
            left++;
        }
        max_width = maxWidthFunc(cur_height*(width),max_width);
    }
    return max_width;
};

const maxWidthFunc=(height,max_width)=>{
    return Math.max(height,max_width);
}
