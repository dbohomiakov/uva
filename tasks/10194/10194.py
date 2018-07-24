import sys


class Tournament:
    def __init__(self, name):
        self.name = name
        self.teams = {}

    def add_team(self, team):
        self.teams[team] = Team(team)

    def add_game(self, game):
        team1, (goals1, goals2), team2 = self._parse_game(game)
        self.teams[team1].add_game(goals1, goals2)
        self.teams[team2].add_game(goals2, goals1)

    def _parse_game(self, game):
        team1, score, team2 = game.strip().split('#')
        score = list(map(int, score.split('@')))
        return team1, score, team2

    def build_table(self):
        table = []
        for idx, team in enumerate(sorted(self.teams.values(),
                                          reverse=True), start=1):
            table.append('{}) {}'.format(idx, team))
        return '\n'.join(table)

    def __str__(self):
        return '\n'.join([self.name, self.build_table()])


class Team:
    def __init__(self, name):
        self.name = name
        self.normalized_name = name.lower()
        self.win = 0
        self.lost = 0
        self.tie = 0
        self.points = 0
        self.goals_scored = 0
        self.goals_against = 0
        self.games = 0

    def add_game(self, goals_scored, goals_against):
        if goals_scored < goals_against:
            self.lost += 1
        elif goals_scored > goals_against:
            self.win += 1
            self.points += 3
        else:
            self.tie += 1
            self.points += 1
        self.goals_scored += goals_scored
        self.goals_against += goals_against
        self.games += 1

    @property
    def goals_diff(self):
        return self.goals_scored - self.goals_against

    def __lt__(self, other):
        return (self.points,
                self.win,
                self.goals_diff,
                self.goals_scored,
                other.games,
                other.normalized_name) < (other.points,
                                          other.win,
                                          other.goals_diff,
                                          other.goals_scored,
                                          self.games,
                                          self.normalized_name)

    def __gt__(self, other):
        return (self.points,
                self.win,
                self.goals_diff,
                self.goals_scored,
                other.games,
                other.normalized_name) > (other.points,
                                          other.win,
                                          other.goals_diff,
                                          other.goals_scored,
                                          self.games,
                                          self.normalized_name)

    def __eq__(self, other):
        return (self.points,
                self.win,
                self.goals_diff,
                self.goals_scored,
                other.games,
                other.normalized_name) == (other.points,
                                           other.win,
                                           other.goals_diff,
                                           other.goals_scored,
                                           self.games,
                                           self.normalized_name)

    def __str__(self):
        return '{} {}p, {}g ({}-{}-{}), {}gd ({}-{})'.format(
            self.name,
            self.points,
            self.games,
            self.win,
            self.tie,
            self.lost,
            self.goals_diff,
            self.goals_scored,
            self.goals_against
        )


if __name__ == '__main__':
    FILE = sys.stdin

    num_cases = int(FILE.readline().strip())

    for t in range(num_cases):
        if t:
            print()

        tournament = Tournament(FILE.readline().strip())

        for _ in range(int(FILE.readline().strip())):
            tournament.add_team(FILE.readline().strip())

        for _ in range(int(FILE.readline().strip())):
            tournament.add_game(FILE.readline().strip())

        print(tournament)
