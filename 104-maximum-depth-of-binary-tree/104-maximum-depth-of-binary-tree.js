/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function(root) {
    let cnt=0;
    function DFS(arr,max){
        if(!arr){
            cnt=cnt>=max?cnt:max;
            return;
        };
        
        DFS(arr.left,max+1);
        DFS(arr.right,max+1);
        
    }
    DFS(root,0);
    return cnt;
};