/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    for(let i=digits.length-1;i>=0;i--){
        if(digits[i]!==9){
            digits[i]+=1;
            return digits;
        }
        digits[i]=0;
        if(i===0){
            digits.unshift(1);
            return digits;
        }
    }
//     let result=[];
//     let num=digits.pop()+1;
//     let ten=false;
//     if(num>=10){
//         ten=true;
//         num=0;   
//     }
//     result.push(num);
//     for(let i=digits.length-1;i>=0;i--){
//         num=digits[i];
//         if(ten){
//             num +=1;   
//         }
        
//         if(num>=10){
//             ten=true;
//             num=0;
//         }else{
//             ten=false;
//         }
//         result.unshift(num);
        
//     }
    
//     if(ten){
//         result.unshift(1);
//     }
//     return result; 
};