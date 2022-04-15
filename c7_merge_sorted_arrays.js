function merge_sorted_arrays(array1, array2) {
    var merged_sorted_array = [];
    var pointer1 = 0;
    var pointer2 = 0;
    while (pointer1 < array1.length || pointer2 < array2.length) {
        if (array1[pointer1] == undefined) {
            merged_sorted_array.push(array2[pointer2]);
            pointer2++;
        }
        if (!array1[pointer2] == undefined) {
            merged_sorted_array.push(array1[pointer1]);
            pointer1++;
        }
        if (array1[pointer1] < array2[pointer2]) {
            merged_sorted_array.push(array1[pointer1]);
            pointer1++;
        }
        if (array2[pointer2] < array1[pointer1]) {
            merged_sorted_array.push(array2[pointer2]);
            pointer2++;
        }
    }
    return merged_sorted_array;
}

console.log(merge_sorted_arrays([6], [3, 9]));
