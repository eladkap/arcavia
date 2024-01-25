class Symbol(object):
    def __init__(self, symbol: str, meaning: str, code: str, category: str):
        self.symbol = symbol
        self.meaning = meaning
        self.code = code
        self.category = category

    def __str__(self):
        d = {
            'symbol': self.symbol,
            'meaning': self.meaning
        }
        return str(d)

    def to_dict(self):
        return {
            'symbol': self.symbol,
            'meaning': self.meaning,
            'code': self.code,
            'category': self.category
        }


if __name__ == '__main__':
    symbol = Symbol('!', 'exclamation mark', '12', 'C')
