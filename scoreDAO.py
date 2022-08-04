from DAO import DAO
from score import Score

class ScoreDAO(DAO):
    def __init__(self):
        super().__init__('score.pkl')

    def add(self, data: str, score: Score):
        if (score is not None) and (isinstance(score, Score)):
            super().add(data, score.score)
    
    def get_all(self):
        return super().get_all()