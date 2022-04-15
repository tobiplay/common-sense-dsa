function hundred_sum(array) {
    let leftPointer = 0;
    let rightPointer = array.length - 1;

    while (leftPointer < array.length / 2) {
        if (array[leftPointer] + array[rightPointer] != 100) {
            return false;
        }

        leftPointer++;
        rightPointer--;
    }

    return true;
}

console.log(hundred_sum([100, 99, 98, 2, 1, 0]));
