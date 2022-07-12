 /*
 1. 공백은 무시
 2. "-"일경우 음수, "+"혹은 아무 부호가 없을경우는 양수. 
 단, "-"과"+"이 문자열 끝에있지 않을 경우만 읽어옴.
 3. 다음 문자가 숫자가 아닐때까지 읽어옵니다. 나머지 문자열은 무시합니다.
 4. 읽어온 숫자를 integer형식으로 바꿔줍니다. ("0032"=>32,"123"=>123). 
 읽어온 숫자가 없으면 0을 리턴해줍니다.
 5. [-2**31, 2**31-1]의 범위에서 벗어나면 아래와같이 숫자를 고정시켜줍니다. 
 -2**31보다 작을 경우 -2**31로, 2**31-1보다 클 경우 2**31-1로 고정시킵니다.
 6. 읽은 integer이 마지막 결과입니다.
 
 
 */

const myAtoi = function(s) {
    let answer='';
    let sign=false;
    const maxNum = (2**31)-1;
    const minNum=(-2)**31;
    s=s.trim();
    for(let i=0;i<s.length;i++){
        if(i===0&&s[i]==="-"){
            sign=true;
            continue;
        }else if(i===0&&s[i]==="+"){
            continue;
        }
        if(!isNaN(s[i])&&s[i]!==" "){
            answer+=s[i];
            continue;
        }else{
            break;
        }
    }
    answer = sign?Number(answer)*-1:Number(answer);
    if(answer<minNum){
        return minNum;
    }else if(answer>maxNum){
        return maxNum;
    }else{
        return answer;
    }
    
    
};