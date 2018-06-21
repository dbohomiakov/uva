import sys


def parse_variables(line):
    return list(map(int, line.strip().split()))


if __name__ == '__main__':
    file = sys.stdin

    while True:
        liquidity_status = 'S'
        line = file.readline().strip()

        if line == '0 0':
            break

        numb_banks, num_debentures = parse_variables(line)
        monetary_reserves = parse_variables(file.readline())

        for _ in range(num_debentures):
            debtor_bank, credit_bank, debenture = parse_variables(file.readline())
            monetary_reserves[debtor_bank - 1] -= debenture
            monetary_reserves[credit_bank - 1] += debenture
    
        print(('S', 'N')[any(n<0 for n in monetary_reserves)])
