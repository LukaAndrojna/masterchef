from random import random, sample

from numpy.random import normal

from models.competitor import Competitor

def set_skill() -> float:
    return normal(loc=2, scale=1, size=1)[0]

def set_ambition() -> float:
    return abs(normal(loc=0.5, scale=0.1, size=1)[0])

class Competition:
    def __init__(self, competitors_n: int):
        self._competitors = {f'{i}': Competitor(set_skill(), set_ambition()/10) for i in range(competitors_n-1)}
        avg_skill = sum([competitor.get_skill() for competitor in self._competitors.values()]) / (competitors_n-1)
        avg_skill *= 1.2
        self._competitors['avg'] = Competitor(avg_skill, 0.1)
        self._avg_position = 20
    
    def __str__(self) -> str:
        return ', '.join(list(self._competitors.keys()))

    def elimination_round(self):
        keys = list(self._competitors.keys())
        elim_len = len(keys)
        if elim_len > 5:
            elim_len -= 3
        elim = sample(keys, elim_len)

        loser = ''
        min_score = 100

        for key in elim:
            competitor_score = self._competitors[key].compete()
            if competitor_score < min_score:
                loser = key
                min_score = competitor_score

        if loser == 'avg':
            self._avg_position = len(self._competitors)
        del self._competitors[loser]

    def run(self) -> str:
        for _ in range(len(self._competitors)-1):
            self.elimination_round()
        return self._avg_position
