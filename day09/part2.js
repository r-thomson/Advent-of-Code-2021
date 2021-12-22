const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(path.join(__dirname, 'input.txt')).toString().trim().split('\n');
const heightMap = input.map(line => line.split('').map(char => Number.parseInt(char)));

const lowPoints = [];
const flowMap = {}; // High points that flow to low points

for (let i = 0; i < heightMap.length; i++) {
    for (let j = 0; j < heightMap[i].length; j++) {
        const adjacent = {};
        for (let [_i, _j] of [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]) {
            adjacent[_i + ',' + _j] = heightMap[_i]?.[_j] ?? Number.Infinity;
        }
        const sortedAdj = Object.values(adjacent).sort((a, b) => a - b);

        if (sortedAdj[0] > heightMap[i][j]) {
            lowPoints.push(i + ',' + j);
        } else if (sortedAdj[0] < heightMap[i][j] && heightMap[i][j] < 9) {
            flowMap[i + ',' + j] = Object.keys(adjacent).find(k => adjacent[k] === sortedAdj[0]);
        }
    }
}

const getFlowsInto = (low) => {
    return Object.keys(flowMap)
        .filter(hi => flowMap[hi] === low)
        .map(getFlowsInto)
        .reduce((acc, val) => acc + val, 1);
}

console.log(lowPoints.map(getFlowsInto).sort((a, b) => b - a).slice(0, 3).reduce((a, el) => a * el, 1));
