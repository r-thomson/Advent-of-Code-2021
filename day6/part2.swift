import Foundation

let inputURL = URL(fileURLWithPath: "input.txt", relativeTo: URL(fileURLWithPath: #filePath))
let input = try! String(contentsOf: inputURL).trimmingCharacters(in: .whitespacesAndNewlines)

var state = [Int: Int]()
for number in input.split(separator: ",").compactMap({ Int($0) }) {
    state[number, default: 0] += 1
}

for _ in 0..<256 {
    state = tick(state: state)
}

print(state.values.reduce(0, +))

func tick(state: [Int: Int]) -> [Int: Int] {
    var newState = [Int: Int]()
    for (age, count) in state {
        if age == 0 {
            newState[8, default: 0] += count // Reset these fish
            newState[6, default: 0] += count // New fish
        } else {
            newState[age - 1, default: 0] += count
        }
    }
    return newState
}
