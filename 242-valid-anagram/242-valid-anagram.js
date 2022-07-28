/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if(s.length!==t.length) return false
    const arr1=s.split("").sort();
    const arr2=t.split("").sort();
    for(let i=0;i<arr1.length;i++){
        if(arr1[i]!==arr2[i]) return false;
    }
    return true;
};