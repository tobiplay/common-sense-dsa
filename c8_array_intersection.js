// The alogrithm should have O(N) by design
function arrayIntersection(array1, array2) {
    var intersectedArray = [];
    var numbersHashTable = {};
    for (var _i = 0, array1_1 = array1; _i < array1_1.length; _i++) {
        var value = array1_1[_i];
        numbersHashTable[value] = true;
    }
    for (var _a = 0, array2_1 = array2; _a < array2_1.length; _a++) {
        var value = array2_1[_a];
        if (numbersHashTable[value]) {
            intersectedArray.push(value);
        }
    }
    return intersectedArray;
}
console.log(arrayIntersection([1, 2, 3, 4, 5], [0, 2, 4, 6, 8])); // -> [2, 4]
