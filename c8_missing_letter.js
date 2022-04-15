function returnMissingLetter(string) {
    var lowercaseAlphabet = "abcdefghijklmnopqrstuvwxyz";
    var knownLetters = {};
    for (var i = 0; i < string.length; i++) {
        knownLetters[string[i]] = true;
    }
    for (var j = 0; j < lowercaseAlphabet.length; j++) {
        if (!knownLetters[lowercaseAlphabet[j]]) {
            return lowercaseAlphabet[j];
        }
    }
}
console.log(returnMissingLetter("the quick brown box jumps over a lazy dog"));
