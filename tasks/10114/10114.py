import sys
from decimal import Decimal
from collections import namedtuple


Loan = namedtuple('Loan', 'period down_payment amount deprecation_months')


def parse_deprecations(line):
    variables = line.strip().split()
    return {int(variables[0]): Decimal(variables[1])}


def parse_loan(line):
    variables = line.strip().split()
    return Loan(int(variables[0]),
                Decimal(variables[1]),
                Decimal(variables[2]),
                int(variables[3]))


def main(loan, deprecations):
    complete_month = 0
    deprecation = deprecations[0]
    loan_amount = loan.amount
    car_price = (loan_amount + loan.down_payment) * (1 - deprecation)

    # TODO: Refactor dry
    if car_price > loan_amount:
        return complete_month

    month_payment = loan.amount / loan.period

    for month in range(1, loan.period + 1):
        deprecation = deprecations.get(month, deprecation)
        car_price = car_price * (1 - deprecation)
        loan_amount -= month_payment

        if car_price > loan_amount:
            complete_month = month
            break
    return complete_month


if __name__ == '__main__':
    loan = None
    deprecations = {}

    for line in sys.stdin:

        if not loan:
            loan = parse_loan(line)
            if loan.period < 0:
                break
            continue

        # TODO: Refactor dry
        if len(deprecations) != loan.deprecation_months:
            deprecations.update(parse_deprecations(line))
            if len(deprecations) != loan.deprecation_months:
                continue

        month = main(loan, deprecations)
        print('{} month{}'.format(month, ['s', ''][month == 1]))

        loan = None
        deprecations = {}
