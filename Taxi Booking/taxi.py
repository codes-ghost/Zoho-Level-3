class Taxi:
    def __init__(self, Id):
        self.taxiId = Id
        self.currentPoint = "A"
        self.earnings = 0
        self.freeTime = 6
        self.journeyDetails = []