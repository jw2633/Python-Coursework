class Fish(object):    
    school = []

    @staticmethod
    def remaining():
        print("Number of fish in the pond:", len(Fish.school))

        for fish in Fish.school:
            print(fish)

    @staticmethod
    def largest():
        if len(Fish.school) > 0:
            Fish.school.sort()

            print("The largest fish is:", Fish.school[-1].name, "\n")
        else:
            print("No fish in pond.")


    def __init__(self, name, length):
        print("Fish put in pond:", name, "\n")
        self.name = name
        self.length = length
        self.caught = False
        Fish.school.append(self)

    def __str__(self):
        reply = "Name: " + self.name + "\n"
        reply += "Length: " + str(self.length) + "\"\n"
        if self.caught:
            reply += "Status: CAUGHT\n"
        else:
            reply += "Status: FREE\n"
        return reply

    def __gt__(self, other):
        if self.length > other.length:
            return True
        else:
            return False

    def catch(self):
        print("You attempt to catch " + self.name + ".", end=' ')
        if not self.caught:
            print("Success!")
            self.caught = True
            print(self)
            Fish.school.remove(self)
        else:
            print(self.name, "was already caught!\n")

class StealthFish(Fish):
    def catch(self):
        print("You attempt to catch " + self.name + ".", end = ' ')
        print("But it can't be done!!!\n")

class FancyFish(Fish):
    def __init__(self, title, name, length):
        super().__init__(name, length)
        self.title = title

    def catch(self):
        super().catch()
        print("What a rude thing to do to", self.title, self.name, "!\n")

class NiceFish(Fish):
    def release(self):	
        print("You attempt to release " + self.name + ".", end = ' ')
        if self.caught:	
            print("Success!")
            self.caught = False
            print(self)
            Fish.school.append(self)
        else:
            print(self.name, "was already free!\n")

#test code
fish1 = StealthFish("007", 11)
fish2 = FancyFish("Lord","Grantham", 10)
fish3 = NiceFish("Nemo", 3)
fish1.catch()
fish2.catch()
fish3.catch()
fish3.release()
fish3.release()
Fish.remaining()

