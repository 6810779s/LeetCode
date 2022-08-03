


var MyCalendar = function() {
    let result=[];
    this.result=result;
    
};

/** 
 * @param {number} start 
 * @param {number} end
 * @return {boolean}
 */
MyCalendar.prototype.book = function(start, end) {
    const resultLen=this.result.length
    if(resultLen===0){
        this.result.push([start,end]);
        return true;
    }
    
    for(let i=0;i<resultLen;i++){
        const res=this.result[i];
        if((start>=res[0]&&start<res[1])||(end>res[0]&&start<=res[0])){
            console.log("[start,end]:",[start,end],"res",res,"i:",i)
            return false;
        }
    }
    
    this.result.push([start,end]);
    return true;
};

/** 
 * Your MyCalendar object will be instantiated and called as such:
 * var obj = new MyCalendar()
 * var param_1 = obj.book(start,end)
 */