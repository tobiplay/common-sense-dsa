function productsTwoArrays(array1, array2) {
    var allProducts = [];
    for (var i = 0; i < array1.length; i++) {
        for (var j = 0; j < array2.length; j++) {
            allProducts.push(array1[i] * array2[j]);
        }
    }
    return allProducts;
}
console.log(productsTwoArrays([1, 2, 3], [10, 100, 1000]));
