import sys

WORD_MAPPING = {'one': 1, 'two': 2, 'three': 3}


def recognize_word(written_word):
    for word in WORD_MAPPING:
        if len(word) == len(written_word):
            if sum([x != y for x, y in zip(word, written_word)]) in [1, 0]:
                return WORD_MAPPING[word]


def main(line):
    print(recognize_word(line))


if __name__ == '__main__':
    for idx, line in enumerate(sys.stdin):
        if not idx:
            continue
        
        main(line.strip())
