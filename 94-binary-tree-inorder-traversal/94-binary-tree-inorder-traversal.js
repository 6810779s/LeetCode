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
 * @return {number[]}
 */
var inorderTraversal = function(root) {
    let answer = [];
    
    function inorder(arr){
        if(!arr) return;
        inorder(arr.left);
        answer.push(arr.val);
        inorder(arr.right);
        
    }
    inorder(root);
    return answer;
};