/**
 * @param {number} x
 * @return {number}
 */

// 이진 탐색
var mySqrt = function(x) {
    if(x===0||x===1) return x;
    let start=0;
    let end=parseInt(x/2)+1;
    let mid=0;
    
    while(end-start>1){
        mid=parseInt((start+end)/2);
        if(mid*mid===x){
            return mid;
        }else if(mid*mid>x){
            end=mid;
        }else if(mid*mid<x){
            start=mid;
        }
        
    }
    return start;
};

