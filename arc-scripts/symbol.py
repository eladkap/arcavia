class Symbol(object):
    def __init__(self, symbol_id: str, symbol: str, title: str, category: str):
        self.symbol_id = symbol_id
        self.symbol = symbol
        self.title = title
        self.category = category

    def __str__(self):
        d = {
            'symbol_id': self.symbol_id,
            'symbol': self.symbol,
            'title': self.title,
            'category': self.category
        }
        return str(d)

    def to_dict(self):
        return {
            'symbol_id': self.symbol_id,
            'symbol': self.symbol,
            'title': self.title,
            'category': self.category
        }
