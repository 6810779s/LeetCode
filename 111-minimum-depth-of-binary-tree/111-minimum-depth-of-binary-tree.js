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


var minDepth = function(root) {
    let min=Infinity;
    function DFS(node){
        if(!node) return 0;
        
        if(!node.left) return DFS(node.right)+1;
        if(!node.right) return DFS(node.left)+1;
        
        const leftDepth=DFS(node.left);
        const rightDepth=DFS(node.right);
        
       
        console.log(leftDepth,rightDepth)
        return 1+Math.min(leftDepth,rightDepth);
//         console.log("left:",leftDepth,"right:",rightDepth);
//         if(min===Infinity){
//             min=Math.min(leftDepth,rightDepth);
//         }else{
//             min=Math.min(min,leftDepth,rightDepth);
//         }
        
//         return min;
    }
    return DFS(root);
};