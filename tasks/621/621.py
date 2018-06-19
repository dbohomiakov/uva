import sys
import re
from collections import OrderedDict


SEARCH_PATTERNS = OrderedDict([
    ('+', re.compile('^(1|4|78)$')),
    ('-', re.compile('^(\d)+35$')),
    ('*', re.compile('^9(\d)+4$'))
])


def decrypt_experiment(encrypted_result):
    result = '?'

    for k, v in SEARCH_PATTERNS.items():
        if re.search(v, encrypted_result):
            result = k
            break

    return result


def main(line):
    return decrypt_experiment(line)


if __name__ == '__main__':
    for idx, line in enumerate(sys.stdin):
        if not idx:
            continue

        print(main(line.strip()))
