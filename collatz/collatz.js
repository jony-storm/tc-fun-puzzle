// function ndigit(n) {
//     let num = "9"
//     for(let i =0; i<(n-1); i++) {
//         num += Math.floor(Math.random()*10)
//     }
//     return num
// }

function ndigit(n) {
    let num = ""
    let firstdigit = 0
    do {
    	firstdigit = Math.floor(Math.random()*10)
    }
    while(firstdigit == 0)
    num += firstdigit
    for(let i =0; i<(n-1); i++) {
        num += Math.floor(Math.random()*10)
    }
    return num
}

function collatz(n) {
    let num = BigInt(n);
    // console.log(num);
    let total_stopping_time = 0;
    while(num != 1n){
      if(num % 2n == 0n){
        num = num / 2n; 
        total_stopping_time += 1;
      } else{
        num = (num * 3n) + 1n;
        total_stopping_time += 1;
      }
    }
    return total_stopping_time;
}

// function ndigit(n) {
//     let num = "9"
//     function randBet(min, max) { // min and max included 
//         return Math.floor(Math.random() * (max - min + 1) + min)
//     }

//     for(let i =0; i<(n-1); i++) {
//         num += randBet(5,9)
//     }
//     return num
// }

function largestCollatz(count, max_digit) {
    let largest = {result: 0, num: 0n};
    // let alllist = []
    for(let i = 0; i < count; i++) {
        let num = ndigit(max_digit);
        let result = collatz(num);

        // alllist.push({result, num})
        if (result > largest.result) {
            largest.result = result
            largest.num = num
        }
    }
    // console.log(alllist)
    return largest
}
console.time("collatz")
let largest_result = largestCollatz(process.argv[2], process.argv[3]);
console.log(largest_result)
console.timeEnd("collatz")

// let tst = collatz('9789402305002136487093906844708122603132388728000699389772422068388744250171275638655545857499554219')
// console.log(tst);