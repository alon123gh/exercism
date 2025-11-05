class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def add_score(self, score):
        self.scores.append(score)

    def latest(self):
        if self.scores:
            return self.scores[-1]
        return None
    def personal_top_three(self):
        return sorted( self.scores, reverse=True )[:3]

    def personal_best(self):
        return max(self.scores)

    
