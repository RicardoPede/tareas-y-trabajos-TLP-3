function add(a, b) {
    while (b != 0) {
        let carry = a & b;
        a = a ^ b;
        b = carry << 1;
    }
    return a;
}

let num1 = process.argv[2];
let num2 = process.argv[3];
console.log(add(num1, num2));