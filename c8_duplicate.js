function findFirstDuplicate(array) {
    var hashTable = {};
    for (var i = 0; i < array.length; i++) {
        if (hashTable[array[i]]) {
            return array[i];
        }
        else {
            hashTable[array[i]] = true;
        }
    }
}
console.log(findFirstDuplicate(["a", "b", "c", "d", "c", "e", "f"])); // -> "c"
