function returnMissingLetter(string: string): string {
    let lowercaseAlphabet = "abcdefghijklmnopqrstuvwxyz";
    let knownLetters: { [key: string]: boolean } = {};

    for (let i = 0; i < string.length; i++) {
        knownLetters[string[i]] = true;
    }

    for (let j = 0; j < lowercaseAlphabet.length; j++) {
        if (!knownLetters[lowercaseAlphabet[j]]) {
            return lowercaseAlphabet[j];
        }
    }
}

console.log(returnMissingLetter("the quick brown box jumps over a lazy dog"));
