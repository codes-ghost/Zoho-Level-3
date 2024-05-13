class Taxi:
    def __init__(self, id):
        self.id = id
        self.currentPoint = "a"
        self.earnings = 0
        self.journeyDetails = []
        self.freeTime = 6