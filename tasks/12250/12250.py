import sys


LANGUAGE_MAPPING = {
    'HELLO': 'ENGLISH',
    'HOLA': 'SPANISH',
    'HALLO': 'GERMAN',
    'BONJOUR': 'FRENCH',
    'CIAO': 'ITALIAN',
    'ZDRAVSTVUJTE': 'RUSSIAN'
}

def main(line, case_number):
    lang = LANGUAGE_MAPPING.get(line, 'UNKNOWN')
    print(f'Case {case_number + 1}: {lang}')


if __name__ == '__main__':
    for idx, line in enumerate(sys.stdin):
        if line.strip() == '#':
            break
        main(line.strip(), idx)
