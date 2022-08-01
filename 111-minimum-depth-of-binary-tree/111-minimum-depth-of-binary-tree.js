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
const MAX = Math.pow(10, 5) + 1;

const searchMinDepth = (root, depth) => {
  if (root === null) return MAX;
  depth++;

  if (root.left === null && root.right === null) return depth;

  const leftMin = searchMinDepth(root.left, depth);
  const rightMin = searchMinDepth(root.right, depth);

  const min = Math.min(leftMin, rightMin);
  return min;
};

const minDepth = (root) => {
  if (root === null) return 0;
  const value = searchMinDepth(root, 0);
  return value === MAX ? 1 : value;
};

// var minDepth = function(root) {
//     let min=Infinity;
//     function DFS(node){
//         if(!node) return 0;
        
//         console.log("node.val:",node.val);
//         console.log("node.left:",node.left,"node.right:",node.right);
//         if(!node.left) return DFS(node.right)+1;
//         if(!node.right) return DFS(node.left)+1;
        
//         const leftDepth=DFS(node.left);
//         const rightDepth=DFS(node.right);
        
//         console.log("leftDepth:",leftDepth,"rightDepth:",rightDepth);
//         return 1+Math.min(leftDepth,rightDepth);
//     }
//     return DFS(root);
// };