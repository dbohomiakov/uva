import sys


class Journal:
    def __init__(self, tolls):
        self.vehicles = {}
        self.tolls = self._parse(tolls)

    def _parse(self, tolls):
        return {idx: int(v) for idx, v in enumerate(tolls.strip().split())}

    def _parse_travel(self, travel):
        return travel.strip().split()

    def append(self, travel):
        lic, timestamp, direction, distance = self._parse_travel(travel)
        vehicle = self.vehicles.setdefault(lic, Vehicle(lic))
        vehicle.add_travel(timestamp, direction, distance)

    def generate_report(self):
        report = []

        for lic in sorted(self.vehicles):
            bill = self.vehicles[lic].calc_bill(self.tolls)

            if bill:
                report.append('{} ${:.2f}'.format(lic, bill / 100))

        return '\n'.join(report)


class Vehicle:
    def __init__(self, lic):
        self.travels = []
        self.license = lic
        self.travel_length = 0

    def add_travel(self, timestamp, direction, distance):
        self.travels.append(Travel(timestamp, direction, distance))
        self.travel_length += 1

    def sort_travels(self):
        self.travels.sort(key=lambda x: x.timestamp)

    def calc_bill(self, tolls):
        self.sort_travels()

        bill = 0

        if self.travel_length < 2:
            return bill

        for idx in range(1, self.travel_length):
            prev = self.travels[idx - 1]
            curr = self.travels[idx]

            if (prev.direction, curr.direction) == ('enter', 'exit'):
                bill += abs(prev.distance - curr.distance) * tolls[prev.timestamp.hour] + 100  # noqa

        return bill + 200 if bill else bill

    def __repr__(self):
        return self.license


class Travel:
    def __init__(self, timestamp, direction, distance):
        self.timestamp = Date(timestamp)
        self.distance = int(distance)
        self.direction = direction

    def __lt__(self, other):
        return self.timestamp < other.timestamp

    def __gt__(self, other):
        return self.timestamp > other.timestamp

    def __eq__(self, other):
        return self.timestamp == other.timestamp

    def __repr__(self):
        return '{} {}'.format(self.timestamp, self.distance)


class Date:
    def __init__(self, date):
        self.month, self.day, self.hour, self.minute = self._parse(date)

    def _parse(self, date):
        return list(map(int, date.strip().split(':')))

    def __lt__(self, other):
        return (self.day, self.hour, self.minute) < (other.day,
                                                     other.hour,
                                                     other.minute)

    def __gt__(self, other):
        return (self.day, self.hour, self.minute) > (other.day,
                                                     other.hour,
                                                     other.minute)

    def __eq__(self, other):
        return (self.day, self.hour, self.minute) == (other.day,
                                                      other.hour,
                                                      other.minute)

    def __repr__(self):
        return '{}:{}:{}:{}'.format(self.month, self.day,
                                    self.hour, self.minute)


if __name__ == '__main__':
    file = sys.stdin

    test_cases = int(file.readline().strip())
    file.readline()  # skip blank line in the input

    for i in range(test_cases):
        if i:
            print()  # blank line in the end of each case except last one

        tolls_rec = file.readline()
        journal = Journal(tolls_rec)

        while True:
            rec = file.readline().strip()
            if not rec:
                break
            journal.append(rec)

        print(journal.generate_report())
