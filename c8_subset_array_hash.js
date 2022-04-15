function arraySubset(array1, array2) {
    var largerArray;
    var smallerArray;
    if (array1.length > array2.length) {
        largerArray = array1;
        smallerArray = array2;
    }
    else {
        largerArray = array2;
        smallerArray = array1;
    }
    var hashTable = {};
    for (var _i = 0, largerArray_1 = largerArray; _i < largerArray_1.length; _i++) {
        var value = largerArray_1[_i];
        hashTable[value] = true;
    }
    for (var _a = 0, smallerArray_1 = smallerArray; _a < smallerArray_1.length; _a++) {
        var value = smallerArray_1[_a];
        if (!hashTable[value]) {
            return false;
        }
    }
    return true;
}
console.log(arraySubset(["a", "b", "c", "d", "e", "f"], ["b", "d", "f"]));
