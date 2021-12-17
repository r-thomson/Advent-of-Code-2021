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
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

const errorScores = input.map(line => {
    const stack = [];

    for (const char of line) {
        if (Object.keys(pairs).includes(char)) {
            stack.push(char);
        } else {
            if (char !== pairs[stack.pop()]) {
                return scores[char];
            }
        }
    }

    return 0;
});

console.log(errorScores.reduce((a, b) => a + b, 0));
