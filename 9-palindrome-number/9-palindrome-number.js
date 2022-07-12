/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    const x_reverse = String(x).split("").reverse().join("");
    if(Number(x_reverse)===x){
        return true;
    }
    return false;
};