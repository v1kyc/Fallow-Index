class MultiMultiSet:

    """Represents a single Multi Multi draw."""

    POOL_SIZE = 80
    DRAW_COUNT = 20
    TICKET_COST = 2.50

    PRIZE_TABLE = [0,0,0,0,2,4,12,140,520,10000,250000]

    def serialise(self, number):
        return {
            "number":number,
            "drawn": "",
            "hits": "",
            "prize": ""
        }