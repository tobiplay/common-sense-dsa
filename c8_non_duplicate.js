function nonDuplicate(string) {
    var duplicates = {};
    for (var i = 0; i < string.length; i++) {
        if (!duplicates[string[i]]) {
            duplicates[string[i]] = 1;
        }
        else {
            duplicates[string[i]]++;
        }
    }
    for (var j = 0; j < string.length; j++) {
        if (duplicates[string[j]] == 1) {
            return string[j];
        }
    }
}
console.log(nonDuplicate("minimum"));
