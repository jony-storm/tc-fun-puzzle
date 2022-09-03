const crypto = require('crypto')
// function ndigit(n) {
//     let num = "9"
//     for(let i =0; i<(n-1); i++) {
//         num += Math.floor(Math.random()*10)
//     }
//     return num
// }

// function ndigit(n) {
//     let num = ""
//     let firstdigit = 0
//     do {
//     	firstdigit = Math.floor(Math.random()*10)
//     }
//     while(firstdigit == 0)
//     num += firstdigit
//     for(let i =0; i<(n-1); i++) {
//         num += Math.floor(Math.random()*10)
//     }
//     return num
// }

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

function ndigit(n, biased=0, mini=0, maxi=9) {
    let num = ""
    
    let j = 0 
    // console.log("mini maxi " + mini + " " + maxi + " biased " + biased); 9996436752125763126813368707230884145124147183356702180352743766745360458725666226350612476377162073
    if (biased > 0) {
      for(let i =0; i<biased; i++) {
        num += crypto.randomInt(parseInt(mini),parseInt(maxi))
        j++
      }
    }
    for(let i =j; i<n; i++) {
        num += crypto.randomInt(0,9)
    }
    return num
}

function largestCollatz(count, max_digit, biased, min, max) {
    let largest = {result: 0, num: 0n};
    // let alllist = []
    for(let i = 0; i < count; i++) {
        let num = ndigit(max_digit, biased, min, max);
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
let largest_result = largestCollatz(process.argv[2], process.argv[3], process.argv[4], process.argv[5], process.argv[6]);
// for(let i=0; i < process.argv[2]; i++) {
//   // console.log("random between " + randBet2(7,9));
//   console.log(ndigit(process.argv[3], process.argv[4], process.argv[5], process.argv[6]));
// }
console.log(largest_result)//
console.timeEnd("collatz")

// let tst = collatz('9789402305002136487093906844708122603132388728000699389772422068388744250171275638655545857499554219')
// console.log(tst); // 0000000000000003704581464390686238882103504581845607364239825257695114298180015970644459945543299520