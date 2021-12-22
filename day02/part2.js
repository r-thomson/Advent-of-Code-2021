const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(path.join(__dirname, 'input.txt')).toString().trim().split('\n');

let horizontal = 0;
let depth = 0;
let aim = 0;

for (const command of input) {
    let [, dir, dist] = command.match(/([a-z]+) ([0-9]+)/);
    dist = Number.parseInt(dist);

    if (dir === 'forward') {
        horizontal += dist;
        depth += aim * dist;
    } else if (dir === 'down') {
        aim += dist;
    } else if (dir === 'up') {
        aim -= dist;
    } else {
        throw Error();
    }
}

console.log(horizontal * depth);
