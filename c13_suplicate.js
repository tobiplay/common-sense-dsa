function hasDuplicateValue(array) {
    // Presort the array:
    // (In JavaScript, the following usage of the sort function
    // is required to ensure that the numbers are in numerical order,
    // instead of "alphabetical" order.)

    array.sort((a, b) => (a < b ? -1 : 1));

    // Iterate through the values in the array up until the last one:
    for (let i = 0; i < array.length - 1; i++) {
        // If the value is identical to the next value
        // in the array, we found a duplicate:

        if (array[i] == array[i + 1]) {
            return true;
        }
    }

    // If we get to the end of the array without having
    // returned true, it means there are no duplicates:
    return false;
}

console.log(hasDuplicateValue([1, 5, 2, 4, 9]))
