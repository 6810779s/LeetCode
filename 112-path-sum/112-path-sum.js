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
 * @param {number} targetSum
 * @return {boolean}
 */
var hasPathSum = function(root, targetSum) {
    let bool=false;
    function DFS(node,sum){
        if(!node) return;
        if(!node.left&&!node.right){
            if(sum+node.val===targetSum){
                bool=true;
                return;
            }
        }
        DFS(node.left,sum+node.val);
        DFS(node.right,sum+node.val);
    }
    DFS(root,0);
    return bool;
};