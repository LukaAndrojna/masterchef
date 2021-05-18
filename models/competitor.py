from numpy.random import normal


class Competitor:
    def __init__(self, skill: float=0.5, ambition: float=0.1):
        self._loc = skill
        self._scale = ambition #cap_score()

    def __str__(self) -> str:
        return f'Skill: {self._loc} | Ambition: {self._scale}'

    def get_skill(self) -> float:
        return self._loc

    def get_ambition(self) -> float:
        return self._scale

    def compete(self) -> float:
        return normal(loc=self._loc, scale=self._scale, size=1)[0]
