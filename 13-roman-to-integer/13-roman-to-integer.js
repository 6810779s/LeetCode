/**
 * @param {string} s
 * @return {number}
 */
const romanToInt = function(s) {
    const map = new Map();
    map.set("I",1)
    .set("V",5)
    .set("X",10)
    .set("L",50)
    .set("C",100)
    .set("D",500)
    .set("M",1000)
    let answer=0;
    for(let i=s.length-1;i>-1;i--){
        if(map.get(s[i])<map.get(s[i+1])){
            answer-=map.get(s[i]);
        }else{
            answer+=map.get(s[i]);
        }
    }
    return answer;
        
};