class MultiMultiSet:
    """Represents a single Multi Multi ticket/result."""

    POOL_SIZE = 80
    DRAW_COUNT = 20
    TICKET_COST = 2.50

    PRIZE_TABLE = [0,0,0,0,2,4,12,140,520,10000,250000]

    def __init__(self, numbers):
        self.numbers = numbers
        self.drawn = []
        self.hits = 0
        self.prize = 0

    def serialise(self):
        return {
            "numbers": self.numbers,
            "drawn": self.drawn,
            "hits": self.hits,
            "prize": self.prize
        }