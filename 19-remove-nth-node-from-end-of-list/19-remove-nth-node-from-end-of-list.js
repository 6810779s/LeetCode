/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    let numArr=[];
    let node=head;
    while(node){
        numArr.push(node.val);
        node=node.next;
    }
    head=new ListNode(0,head);
    let prev=head,next=head.next;
    let num= numArr.length-n+1;
    
    console.log(head)
    while(next){
        console.log("prev:",prev,"next:",next,);
        console.log("numArr:",numArr)
          if(numArr.length===n){
              prev.next=next.next;
          }else{
              prev=prev.next;
          }
        numArr.pop();
        next=next.next;
        
    }
    return head.next;
};