function nonDuplicate(string: string): string {
    let duplicates: { [key: string]: number } = {};

    for (let i = 0; i < string.length; i++) {
        if (!duplicates[string[i]]) {
            duplicates[string[i]] = 1;
        } else {
            duplicates[string[i]]++;
        }
    }

    for (let j = 0; j < string.length; j++) {
        if (duplicates[string[j]] == 1) {
            return string[j];
        }
    }
}

console.log(nonDuplicate("minimum"));
