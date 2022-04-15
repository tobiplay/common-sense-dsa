// The alogrithm should have O(N) by design
function arrayIntersection(array1: number[], array2: number[]): number[] {
    let intersectedArray: number[] = [];
    let numbersHashTable: { [key: number]: boolean } = {};

    for (let value of array1) {
        numbersHashTable[value] = true;
    }

    for (let value of array2) {
        if (numbersHashTable[value]) {
            intersectedArray.push(value);
        }
    }

    return intersectedArray;
}

console.log(arrayIntersection([1, 2, 3, 4, 5], [0, 2, 4, 6, 8])); // -> [2, 4]
