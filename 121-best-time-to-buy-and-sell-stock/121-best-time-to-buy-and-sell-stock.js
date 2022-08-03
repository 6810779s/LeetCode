/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let max=0;
    let left=0;
    let right=1;
    while(right<prices.length){
        if(prices[left]>prices[right]){
            left=right;
        }else{
            const profit=prices[right]-prices[left];
            max=Math.max(max,profit);
        }
        right++;
    }
    return max;
//     let result=0;
//     let min=prices[0];
    
//     for(let i=1;i<prices.length;i++){
//         min=Math.min(prices[i],min);
//         result=Math.max(prices[i]-min,result);
//     }
//     return result;
};