function allProducts(array: number[]) {
  let products: number[] = [];

  for (let i = 0; i < array.length; i++) {
    for (let j = i + 1; j < array.length; j++) {
      products.push(array[i] * array[j]);
    }
  }

  return products;
}

console.log(allProducts([1, 2, 3, 4, 5]));
