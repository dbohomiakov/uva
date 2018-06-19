import sys

EVENT_MAPPING = {'Umrah': 'Hajj-e-Asghar', 'Hajj': 'Hajj-e-Akbar'}


if __name__ == '__main__':
    for idx, line in enumerate(sys.stdin):
        if line.strip() == '*':
            break
        
        print('Case {}: {}'.format(idx + 1, EVENT_MAPPING[line.strip()]))
