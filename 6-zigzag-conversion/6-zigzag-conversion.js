var convert = function(s, numRows) {
    const ans =new Array(numRows).fill("");
    let cnt=0;
    let plus=true;
    if(numRows===1){
        return s;
    }
    for(const i of s){
        ans[cnt]+=i;
        if(plus){
            cnt+=1;
        }else{
            cnt-=1;
        }
        if(cnt===0){
            plus=true
        }
        else if(cnt>=numRows-1){
            plus=false;
        }
    }
    return ans.join("")
};