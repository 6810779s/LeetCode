const reverse = function(x) {
    let answer;
    if(x>=0){
        const arr=String(x).split("").reverse().join("");
        answer = Number(arr);
    }else{
        const arr=String(x*-1).split("").reverse().join("");
        answer = Number(arr)*(-1)
    }
      if(answer<(-2)**31||answer>(2**31)-1){
        return 0;
       }
    return answer;
    
};