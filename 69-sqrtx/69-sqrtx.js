/**
 * @param {number} x
 * @return {number}
 */

// 이진 탐색
var mySqrt = function(x) {
    if(x===0||x===1) return x;
    let start=0;
    let end=x;
    let num=0;
    
    while(end-start>1){
        num=parseInt((start+end)/2);
        if(num*num===x){
            return num;
        }else if(num*num>x){
            end=num;
        }else if(num*num<x){
            start=num;
        }
        
    }
    return start;
    
    
};

