function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}

var addTwoNumbers = function(l1, l2) {
    const answer = new ListNode();
    let node = answer;
    let ten=false;
    cal=l1.val+l2.val;
    if(cal>=10){
        ten=true;
    }
    node.val=cal%10;
    while(l1.next||l2.next||ten){
        l1=l1.next||new ListNode(0);
        l2=l2.next||new ListNode(0);
        cal=l1.val+l2.val;
        
        if(ten){
            cal+=1;
            ten=false;
        }
        node.next=new ListNode((cal)%10);
        node=node.next;
        if(cal>=10){
            ten=true;
        }
    }
  
    return answer;
};