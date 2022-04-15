function arraySubset(mainArray, subsetArray) {
    var subsetArrayPointer = 0;
    while (subsetArrayPointer < subsetArray.length) {
        var subsetCharInMainArray = false;
        var mainArrayPointer = 0;
        while (mainArrayPointer < mainArray.length) {
            if (mainArray[mainArrayPointer] == subsetArray[subsetArrayPointer]) {
                subsetCharInMainArray = true;
            }
            mainArrayPointer++;
        }
        if (!subsetCharInMainArray) {
            return false;
        }
        subsetArrayPointer++;
    }
    return true;
}
console.log(arraySubset(["a", "b", "c", "d", "e", "f"], ["b", "d", "f"]));
