function factorial(n) {
    if (n === 0 || n === 1) {
        return 1;
    } else {
        var result = 1;
        for (var i = 2; i <= n; i++) {
            var temp = result;
            for (var j = 1; j < i; j++) {
                temp += result;
            }
            result = temp;
        }
        return result;
    }
}
var num = process.argv[2];
console.log(factorial(num));
