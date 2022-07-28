/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
     let dp = new Array(n+1).fill(0);
    dp[1] = 1;
    dp[2] = 2;
    for (let i = 3; i <= n; i++) {
        dp[i] = dp[i-1] + dp[i-2];
    }
    return dp[n];
    
    
//     let cnt=0;
//     function cnt_step(sum){
//         if(sum>n){
//              return;
//         }
//         if(sum===n) cnt++;
        
//         cnt_step(sum+1);
//         cnt_step(sum+2);
//     }
    
//     cnt_step(0);
//     return cnt;
};