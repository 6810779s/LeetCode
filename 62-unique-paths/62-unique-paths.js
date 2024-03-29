/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function(m, n) {
    const arr_route=Array.from(Array(m),()=>Array(n).fill(0));
    for(let i=0;i<m;i++){
        for(let j=0;j<n;j++){
            if(i===0||j===0) arr_route[i][j]=1;
            else arr_route[i][j]=arr_route[i-1][j]+arr_route[i][j-1];
        }
    }
    return arr_route[m-1][n-1];
};