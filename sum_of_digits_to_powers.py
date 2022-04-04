function sum_dig_pow(a, b){
    let result = [];
    for(let i = a; i < b; i++){
        let iSumSq = i
        .toString()
        .split("")
        .map( (element,index) => element**(index+1))
        .reduce( (acc,c) => acc + c)
        if(i === iSumSq){
            result.push(i) 
        }
    }
    return result
}
