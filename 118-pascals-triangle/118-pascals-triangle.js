/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
    if(numRows===1) return [[1]];
    if(numRows===2) return [[1],[1,1]];
    let result=[[1],[1,1]];
    
    for(let i=1;i<numRows-1;i++){
        let arr=[1];
        for(let j=0;j<i;j++){
            arr.push(result[i][j]+result[i][j+1]);
        }
        arr.push(1)
        result.push(arr)
    }
    return result;
};