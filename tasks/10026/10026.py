import sys
from collections import namedtuple
from functools import cmp_to_key


Job = namedtuple('Job', 'day fine idx')


def parse_vars(line):
    return tuple(map(int, line.strip().split()))


def compare_jobs(x, y):
    return x.day * y.fine - y.day * x.fine
    

def main(jobs):
    jobs.sort(key=cmp_to_key(compare_jobs))


if __name__ == '__main__':
    file = sys.stdin
    test_cases = int(file.readline().strip())

    for ncase in range(test_cases):
        jobs = []
        file.readline()  # skip empty line

        num_jobs = int(file.readline().strip())

        for i in range(num_jobs):
            jobs.append(Job(*parse_vars(file.readline()), i + 1))

        main(jobs)
        print(' '.join([str(job.idx) for job in jobs]))

        if ncase < test_cases - 1:
            print()
