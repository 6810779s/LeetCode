/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let stack=[];
    const obj={"(":")","{":"}","[":"]"};
    for(const sign of s){
        if(obj[sign]){
            stack.push(sign);
        }else{
            const tmp=stack.pop();
            if(obj[tmp]!==sign){
                return false;
            }
        }
        
    }
    return stack.length===0?true:false;
};