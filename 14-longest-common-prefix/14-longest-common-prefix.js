/**
 * @param {string[]} strs
 * @return {string}
 */
const longestCommonPrefix = function(strs) {
    const compare=strs[0];
    let idx=0;   
    let answer ="";
    
    let con=true;
    while(idx<compare.length&&con){
        let letter = compare[idx];
        for(let i=0;i<strs.length;i++){
            if(idx>strs[i].length||strs[i][idx]!==letter){
                con=false;
                break;
            }
            if(i===strs.length-1){
                answer+=letter;
            }
        }
        idx++;
    }
    return answer;
};