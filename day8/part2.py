from os import path

with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as file:
    input = file.read().splitlines()

observed_digits = [tuple([''.join(sorted(s)) for s in part.split(' ')]
                         for part in line.split(' | ')) for line in input]


def get_character_frequencies(string_list):
    unique_chars = set.union(*map(set, string_list))
    return {char: sum((char in s) for s in string_list) for char in unique_chars}


segment_map = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9,
}

unique_length_segments = {
    2: 'cf',  # 1
    3: 'acf',  # 7
    4: 'bcdf',  # 4
    7: 'abcdefg',  # 8
}

signal_frequency = get_character_frequencies(segment_map.keys())


def decode_row(first_ten, last_four):
    scrambled_signal_freq = get_character_frequencies(first_ten)

    identified = {}  # Full signals to numbers
    signal_map = {}  # Scrambled letters to regular letters

    # Figure out the numbers we know for sure based on length
    for letters in first_ten:
        if len(letters) in unique_length_segments:
            identified[letters] = unique_length_segments[len(letters)]

    while len(identified) < 10:
        # Ignoring characters we've already identified, look for more unique frequencies
        for scrambled, unscrambled in identified.items():
            scrambled = set(scrambled) - set(signal_map.keys())
            unscrambled = set(unscrambled) - set(signal_map.values())

            filtered_scrambled_freq = {k: v for k, v in scrambled_signal_freq.items() if k in scrambled}
            filtered_unscrambled_freq = {k: v for k, v in signal_frequency.items() if k in unscrambled}

            for char in scrambled:
                char_freq = filtered_scrambled_freq[char]
                if list(filtered_scrambled_freq.values()).count(char_freq) == 1:
                    signal_map[char] = next(k for k, v in filtered_unscrambled_freq.items() if v == char_freq)

        # Try to figure out more numbers
        for letters in set(first_ten) - set(identified.keys()):
            if all(char in signal_map.keys() for char in letters):
                identified[letters] = ''.join(sorted(signal_map[char] for char in letters))

    output_values = [segment_map[identified[letters]] for letters in last_four]
    return int(''.join(map(str, output_values)))


print(sum(decode_row(*row)for row in observed_digits))
