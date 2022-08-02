/**
 * @param {number[][]} matrix
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function(matrix, k) {
    if(matrix.length===1) return matrix[0][0];
    
    let min=matrix[0][0];
    let max=matrix[matrix.length-1][matrix.length-1];
    
    while(min<=max){
        let mid=parseInt((max-min)/2)+min;
        let cnt=0;
        
        console.log("mid:",mid)
        for(let i=0;i<matrix.length;i++){
            for(let j=0;j<matrix[i].length;j++){
                if (matrix[i][0]>mid) break;
                if(matrix[i][j]<=mid) cnt++;
            }
        }
        if(cnt<k){
            min=mid+1;
        }else{
            max=mid-1;
        }
    }
    return min;
};