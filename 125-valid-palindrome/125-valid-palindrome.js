/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    const reg=/[a-zA-Z0-9]/
    let new_str='';
    for(let i=s.length-1;i>=0;i--){
        if(reg.test(s[i])){
            new_str+=s[i].toLowerCase();
        }
    }
    
    let left=0;
    let right=new_str.length-1;
    while(left<right){
        if(new_str[left]===new_str[right]){
            left++;
            right--;
        }else{
            return false
        }
    }
    return true;

};