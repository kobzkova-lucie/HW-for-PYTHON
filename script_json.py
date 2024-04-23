import json

character_frequency = {}

with open('alice.txt', encoding='utf-8') as file:
    for line in file:
        line = line.replace(' ', '').replace('\n', '')
        for character in line.lower():
            if character in character_frequency:
                character_frequency[character] += 1
            else:
                character_frequency[character] = 1

sorted_frequencies = dict(sorted(character_frequency.items()))

with open('hw01_output.json', 'w', encoding='utf-8') as json_file:
    json.dump(sorted_frequencies, json_file, ensure_ascii=False, indent=4)

