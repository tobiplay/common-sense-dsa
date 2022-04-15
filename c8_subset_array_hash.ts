function arraySubset(array1: string[], array2: string[]) {
    let largerArray;
    let smallerArray;

    if (array1.length > array2.length) {
        largerArray = array1;
        smallerArray = array2;
    } else {
        largerArray = array2;
        smallerArray = array1;
    }

    let hashTable: {} = {};

    for (let value of largerArray) {
        hashTable[value] = true;
    }

    for (let value of smallerArray) {
        if (!hashTable[value]) {
            return false;
        }
    }

    return true;
}

console.log(arraySubset(["a", "b", "c", "d", "e", "f"], ["b", "d", "f"]));
