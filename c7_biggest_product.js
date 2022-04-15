function biggestProduct(array) {
    var i = 0;
    var j = i + 1;
    var k = j + 1;
    var biggestProduct = array[i] * array[j] * array[k];
    while (i < array.length) {
        var j_1 = i + 1;
        while (j_1 < array.length) {
            var k_1 = j_1 + 1;
            while (k_1 < array.length) {
                if (array[i] * array[j_1] * array[k_1] > biggestProduct) {
                    biggestProduct = array[i] * array[j_1] * array[k_1];
                }
                k_1++;
            }
            j_1++;
        }
        i++;
    }
    return biggestProduct;
}

console.log(biggestProduct([1, 2, 3, 4, 5, 6]))