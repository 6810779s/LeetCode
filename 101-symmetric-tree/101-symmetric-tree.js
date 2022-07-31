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
 * @return {boolean}
 */
var isSymmetric = function(root) {
    
    function DFS(l,r){
        if(!l&&!r) return true;
        if(!l||!r) return false;
        if(l.val!==r.val) return false;
        if(!DFS(l.left,r.right)) return false;
        if(!DFS(l.right,r.left)) return false;
        return true;
        
    }
    return DFS(root.left,root.right);
};