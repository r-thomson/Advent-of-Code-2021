const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(path.join(__dirname, 'input.txt')).toString().trim().split('\n');

const mostCommonBit = (bitStrings, n) => {
    const frequency = { '0': 0, '1': 0 };
    bitStrings.forEach(str => frequency[str[n]] += 1)

    return (frequency[1] >= frequency[0]);
}

const filterCommonBits = (negate) => {
    let subset = input;
    for (let i = 0; subset.length > 1; i++) {
        const bit = (mostCommonBit(subset, i) !== negate);
        subset = subset.filter(str => Boolean(+str[i]) === bit);
    }

    return Number.parseInt(subset[0], 2);
};

const oxygen = filterCommonBits(false);
const co2 = filterCommonBits(true);

console.log(oxygen * co2);
