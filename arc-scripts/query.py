class Query:
    def __init__(self, category: str, query: str, answers: list, correct_answer: str, difficulty: int):
        self.category = category
        self.query = query
        self.answers = answers
        self.correct_answer = correct_answer
        self.difficulty = difficulty

    def to_dict(self):
        d = {
            'query': self.query,
            'answers': self.answers,
            'correct': self.correct_answer
        }
        return d

    def __str__(self):
        d = self.to_dict()
        return str(d)
