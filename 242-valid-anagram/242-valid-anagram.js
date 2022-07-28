/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if(s.length!==t.length) return false
    for(let i=0;i<s.length;i++){
        if(s.includes(t[i])){
            s=s.replace(t[i],' ');
        }else{
            return false
        }
    }
    return true;
};