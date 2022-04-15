function allProducts(array) {
    var products = [];
    for (var i = 0; i < array.length; i++) {
        for (var j = i + 1; j < array.length; j++) {
            products.push(array[i] * array[j]);
        }
    }
    return products
}
console.log(allProducts([1, 2, 3, 4, 5]));
