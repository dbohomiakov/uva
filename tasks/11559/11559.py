import sys


def parse_vars(line):
    return list(map(int, line.strip().split()))


def calc_total_price(participants, budget, hotel_price, available_beds):

    if max(available_beds) >= participants:
        total_hotel_price = participants * hotel_price

        if budget >= total_hotel_price:
            return total_hotel_price


def main(file):
    
    while True:
        line = file.readline()
        min_price = None

        if not line:
            break

        meeting = parse_vars(line)

        for _ in range(meeting[2]):
            hotel_price = int(file.readline().strip())
            hotel_beds = parse_vars(file.readline())
            total_hotel_price = calc_total_price(meeting[0],
                                                 meeting[1],
                                                 hotel_price,
                                                 hotel_beds)
            if total_hotel_price:
                if min_price:
                    min_price = min(min_price, total_hotel_price)
                else:
                    min_price = total_hotel_price
            

        print(min_price or 'stay home')


if __name__ == '__main__':
    main(sys.stdin)
