const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(path.join(__dirname, 'input.txt')).toString().trim().split('\n');

const pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

const scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

const autocompleteScores = input.map(line => {
    const stack = [];

    for (const char of line) {
        if (Object.keys(pairs).includes(char)) {
            stack.push(char);
        } else {
            if (char !== pairs[stack.pop()]) {
                return null;
            }
        }
    }

    return stack.reverse().map(char => pairs[char]).reduce((total, char) => (total * 5) + scores[char], 0);
});

const sortedScores = autocompleteScores.filter(score => score !== null).sort((a, b) => a - b);
console.log(sortedScores[(sortedScores.length - 1) / 2]);
