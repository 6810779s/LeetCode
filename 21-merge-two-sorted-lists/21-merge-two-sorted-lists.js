/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
const mergeTwoLists = function(list1, list2) {
    let lst=new ListNode();
    let num=lst;
    
    while(list1&&list2){
        
        if(list1.val>=list2.val){
            num.next=list2;
            list2=list2.next;
            
        }else{
            num.next=list1;
            list1=list1.next
        }
        
        num=num.next;
        
    }
    num.next=list1||list2;
    
    return lst.next;
}
