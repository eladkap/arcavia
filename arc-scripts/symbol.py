class Symbol(object):
    def __init__(self, symbol: str, title: str, category: str):
        self.symbol = symbol
        self.title = title
        self.category = category

    def __str__(self):
        d = {
            'symbol': self.symbol,
            'title': self.title,
            'category': self.category
        }
        return str(d)

    def to_dict(self):
        return {
            'symbol': self.symbol,
            'title': self.title,
            'category': self.category
        }
