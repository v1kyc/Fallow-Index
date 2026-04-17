class MultiMultiSet:
    """Represents a single Multi Multi ticket/result."""

    POOL_SIZE = 80
    DRAW_COUNT = 20
    BET_COUNT = 10
    TICKET_COST = 2.50

    PRIZE_TABLE = [0,0,0,0,2,4,12,140,520,10000,250000]

    def __init__(self, game_id, ticket_id, numbers, drawn):
        self.game_id = game_id
        self.ticket_id = ticket_id

        self.numbers = numbers
        self.drawn = drawn
        self.hits = 0
        self.prize = 0

    def serialise(self):
        return {
            "g_id": self.game_id,
            "t_id": self.ticket_id,
            "numbers": self.numbers,
            "drawn": self.drawn,
            "hits": self.hits,
            "prize": self.prize
        }