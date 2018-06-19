import sys


if __name__ == '__main__':
    account_balance = 0
        
    for idx, line in enumerate(sys.stdin):
        if not idx:
            continue

        if line.strip().startswith('donate'):
            account_balance += int(line.strip().split()[1])
        else:
            print(account_balance)
