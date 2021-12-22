const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(path.join(__dirname, 'input.txt')).toString().trim().split('\n');
const bitCount = input[0].length; // Amount of bits in each diagnostic string

const gamma = [...Array(bitCount).keys()].map(i => {
    const frequency = { '0': 0, '1': 0 };
    input.forEach(str => frequency[str[i]] += 1)

    return (frequency[1] > frequency[0]);
}).reduce((acc, bit) => (acc << 1) + bit, 0);

// Flip all the significant bits in epsilon to get gamma
const epsilon = gamma ^ (2 ** bitCount - 1);

console.log(gamma * epsilon);
