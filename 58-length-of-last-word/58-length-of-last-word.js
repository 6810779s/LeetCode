/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let prev_result='';
    let result=''
    for(let i=0;i<s.length;i++){
        if(s[i]!==" "){
            prev_result+=s[i];
        }else{
            if(prev_result.length>0){
            result=prev_result;
            }
            prev_result='';
        }
        
    }
    return prev_result===""?result.length:prev_result.length;
};