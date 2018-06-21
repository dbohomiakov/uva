import sys
from itertools import cycle


SONG = ('Happy', 'birthday', 'to', 'you',
        'Happy', 'birthday', 'to', 'you',
        'Happy', 'birthday', 'to', 'Rujia',
        'Happy', 'birthday', 'to', 'you')


if __name__ == '__main__':
    num_guests = int(sys.stdin.readline().strip())
    song_length = len(SONG)

    guests = [line.strip() for line in sys.stdin]
    num_cycles = num_guests // song_length + bool(num_guests % song_length)

    for name, word in zip(cycle(guests), num_cycles * SONG):
        print('{}: {}'.format(name, word))
