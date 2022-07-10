var longestPalindrome = function(s) {
    let answer='';
    const getPal = (left,right)=>{
        while(left>=0&&right<s.length&&s[left]===s[right]){
            left--;
            right++;
        }
        return s.substring(left+1,right);
    }

    for(let i=0;i<s.length;i++){
        const pal1 = getPal(i,i);
        const pal2=getPal(i,i+1);
        const pal = pal1.length>=pal2.length?pal1:pal2;
        answer=answer.length>=pal.length?answer:pal;
    }   
    return answer;
};