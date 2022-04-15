function merge_sorted_arrays(array1: number[], array2: number[]) {
    let merged_sorted_array: number[] = [];

    let pointer1: number = 0;
    let pointer2: number = 0;

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

    return merged_sorted_array
}

console.log(merge_sorted_arrays([0, 1, 2, 5], [3, 4, 9]))