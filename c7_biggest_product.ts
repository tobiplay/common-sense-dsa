function biggestProduct(array: number[]) {
    let i: number = 0;
    let j: number = i + 1;
    let k: number = j + 1;

    let biggestProduct: number = array[i] * array[j] * array[k];

    while (i < array.length) {
        let j = i + 1;

        while (j < array.length) {
            let k = j + 1;

            while (k < array.length) {
                if (array[i] * array[j] * array[k] > biggestProduct) {
                    biggestProduct = array[i] * array[j] * array[k];
                }

                k++;
            }

            j++;
        }

        i++;
    }

    return biggestProduct;
}
