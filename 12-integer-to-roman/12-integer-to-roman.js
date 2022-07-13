const intToRoman = function(num) {
    let cnt = 1;
    let prevLetter=0;
    let letter='';
    while(cnt<=String(num).length){
        const cur_num = num%(10**cnt);
        const cur = cur_num-prevLetter;
        prevLetter=cur_num;
        const one = ["I","X","C","M"][cnt-1];
        const two = ["V","L","D"][cnt-1];
        const three = ["X","C","M"][cnt-1];
        const roman={0:"",1:`${one}`,2:`${one}${one}`,3:`${one}${one}${one}`,4:`${one}${two}`,5:`${two}`,6:`${two}${one}`,7:`${two}${one}${one}`,8:`${two}${one}${one}${one}`,9:`${one}${three}`};
     
        
        letter=roman[`${cur/10**(cnt-1)}`]+letter;
        cnt++;
    }
    
    return letter;
};