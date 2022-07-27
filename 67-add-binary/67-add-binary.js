/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
    let len1=a.length-1;
    let len2=b.length-1;
    let sum="";
    let num;
    let binary=false;
    
    for(let i=0;i<Math.max(a.length,b.length);i++){
        num = Number((a[len1-i]||0))+Number((b[len2-i]||0)) ;
        if(binary){
            num+=1;
        }
        if(num>=2){
            binary=true;
            num-=2;
        }else{
            binary=false;
        }
        sum=num+sum;
    }
    if(binary){
        sum=1+sum;
    }
    return sum;
    
};