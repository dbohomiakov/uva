import sys


LINKS_PER_TEST_CASE = 10


def parse_vars(line):
    line = line.strip().split()
    return line[0], int(line[1])


if __name__ == '__main__':
    file = sys.stdin
    test_cases = int(file.readline().strip())
    max_relevance = 0
    links = []
    
    for idx in range(1, test_cases + 1):

        for _ in range(LINKS_PER_TEST_CASE):
            link, relevance = parse_vars(file.readline())

            if relevance == max_relevance:
                links.append(link)
            elif relevance > max_relevance:
                links = [link]
                max_relevance = relevance

        print('Case #{}:'.format(idx), *links, sep='\n')
        links = []
        max_relevance = 0
