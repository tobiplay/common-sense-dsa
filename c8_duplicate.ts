function findFirstDuplicate(array: string[]): string {
    let hashTable: { [key: string]: boolean } = {};

    for (let i = 0; i < array.length; i++) {
        if (hashTable[array[i]]) {
            return array[i];
        } else {
            hashTable[array[i]] = true;
        }
    }
}

console.log(findFirstDuplicate(["a", "b", "c", "d", "c", "e", "f"])); // -> "c"
