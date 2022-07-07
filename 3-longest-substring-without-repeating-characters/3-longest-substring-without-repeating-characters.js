/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let current='';
    let str_length=0;
    for(let i=0;i<s.length;i++){
        let idx=0;
        current=current.substring(current.indexOf(s[i])+1);
        current+=s[i];
        str_length=current.length>str_length?current.length:str_length;
    }
    return str_length;
};