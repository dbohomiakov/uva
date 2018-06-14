import sys
from itertools import cycle


def main(line):
    formatted_line = ''
    odd_replacement = True
    
    for symbol in line.strip():
        if symbol == '"':
            if odd_replacement:
                symbol = "``"
            else:
                symbol = "''"
            odd_replacement = not odd_replacement
        formatted_line += symbol

    print(formatted_line)


if __name__ == '__main__':
    main(sys.stdin.read())
