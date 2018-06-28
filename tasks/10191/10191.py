import sys
from collections import namedtuple


Time = namedtuple('Time', 'hours minutes')

START_TIME = Time(10, 0)
END_TIME = Time(18, 0)


class Event:
    def __init__(self, event):
        self.start, self.end = self.parse_event(event)

    def parse_time(self, event_time):
        return Time(*tuple(map(int, event_time.split(':'))))

    def parse_event(self, event):
        start, end, *_ = event.strip().split()
        return self.parse_time(start), self.parse_time(end)
    

class Scheduler:

    def __init__(self, day, start_day, end_day, events):
        self.start_day = start_day
        self.end_day = end_day
        self.events = [Event(event) for event in events]
        self.day = day

    @staticmethod
    def calc_duration(end, start):
        return (end.hours - start.hours) * 60 + end.minutes - start.minutes

    def calc_max_nap(self):
        if not self.events:
            return (self.calc_duration(self.end_day, self.start_day),
                    self.start_day) 

        self.events.sort(key=lambda x: x.start)

        first_event = self.events[0]
        prev_event_end = first_event.end
        nap_duration = self.calc_duration(first_event.start, self.start_day)
        nap_start = self.start_day

        for event in self.events[1:]:
            if event.start > prev_event_end:
                duration = self.calc_duration(event.start, prev_event_end)
                if duration > nap_duration:
                    nap_duration, nap_start = duration, prev_event_end
                prev_event_end = event.end
            elif event.end > prev_event_end:
                prev_event_end = event.end

        last_duration = self.calc_duration(self.end_day, prev_event_end)
        if last_duration > nap_duration:
            nap_duration, nap_start = last_duration, prev_event_end

        return nap_duration, nap_start

    def get_max_nap(self):
        duration, start = self.calc_max_nap()
        
        hours, minutes = divmod(duration, 60)
        hours = '{} hours and '.format(hours) if hours else ''
        formatted_duration = '{}{} minutes'.format(hours, minutes)
        start_time = '{}:{:02d}'.format(*start)

        return ('Day #{}: the longest nap starts at {} and will last for {}.'
                .format(day, start_time, formatted_duration))


if __name__ == '__main__':
    file = sys.stdin

    for day, line in enumerate(file, start=1):
        events = []
        num_events = int(line)

        for _ in range(num_events):
            events.append(file.readline())

        print(Scheduler(day, START_TIME, END_TIME, events).get_max_nap())
