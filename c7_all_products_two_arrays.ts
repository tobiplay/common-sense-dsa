function productsTwoArrays(array1: number[], array2: number[]) {
    let allProducts: number[] = [];

    for (let i = 0; i < array1.length; i++) {
        for (let j = 0; j < array2.length; j++) {
            allProducts.push(array1[i] * array2[j]);
        }
    }

    return allProducts;
}

console.log(productsTwoArrays([1, 2, 3], [10, 100, 1000]));
