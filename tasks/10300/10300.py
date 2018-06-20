import sys


def parse_farmers_data(line):
    return list(map(int, line.strip().split()))


if __name__ == '__main__':
    file = sys.stdin
    num_cases = int(file.readline())

    for _ in range(num_cases):
        summary_premium = 0
        num_farmers = int(file.readline())

        for __ in range(num_farmers):
            farmer_data = parse_farmers_data(file.readline().strip())
            summary_premium += farmer_data[0] * farmer_data[2]
    
        print(summary_premium)
