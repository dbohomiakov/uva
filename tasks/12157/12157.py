import sys


PACKAGES = (('Mile', 30, 10), ('Juice', 60, 15))


def parse_vars(line):
    return list(map(int, line.strip().split()))


def calc_total_cost(name, period, rate, calls):
    return name, sum((call//period + 1 for call in calls)) * rate


def choose_suitable_package(costs):
    min_cost = costs[0][1]
    names = [costs[0][0]]

    for cost in costs[1:]:
        if cost[1] == min_cost:
            names.append(cost[0])
        elif cost[1] < min_cost:
            min_cost = cost[1]
            names = [cost[0]]
    return ' '.join(names), min_cost


if __name__ == '__main__':
    file = sys.stdin

    test_cases = int(file.readline().strip())

    for idx in range(1, test_cases + 1):
        file.readline() # skip number of calls
        client_calls = parse_vars(file.readline())
        costs = []

        for package in PACKAGES:
             costs.append(calc_total_cost(*package, client_calls))

        print('Case {}: {} {}'.format(idx, *choose_suitable_package(costs)))
