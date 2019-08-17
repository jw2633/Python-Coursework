class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

class Container(object):
    def __init__(self, max_cap):
        self.max_cap = max_cap
        self.current = 0

class Course(object):
    def __init__(self, number, hours, time, location, instructor):
        self.number = number
        self.hours = hours
        self.time = time
        self.location = location
        self.instructor = instructor

#main
draw = Card("Spades", "8")
box = Container(10)
i210 = Course("I210", 8, "2:30PM", "BH 330", "James Wang")
