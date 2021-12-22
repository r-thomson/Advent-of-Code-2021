const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(path.join(__dirname, 'input.txt')).toString().trim().split('\n');
const heightMap = input.map(line => line.split('').map(char => Number.parseInt(char)));

const lowPoints = [];

for (let i = 0; i < heightMap.length; i++) {
    for (let j = 0; j < heightMap[i].length; j++) {
        const point = heightMap[i][j];
        let isLowest = true;
        isLowest &&= (heightMap[i + 1]?.[j] ?? Infinity) > point;
        isLowest &&= (heightMap[i - 1]?.[j] ?? Infinity) > point;
        isLowest &&= (heightMap[i]?.[j + 1] ?? Infinity) > point;
        isLowest &&= (heightMap[i]?.[j - 1] ?? Infinity) > point;
        if (isLowest) {
            lowPoints.push(point);
        }
    }
}

const getRiskLevel = height => height + 1;

console.log(lowPoints.reduce((acc, height) => acc + getRiskLevel(height), 0));
