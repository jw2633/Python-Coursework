class Place(object):
    place_list = []

    @staticmethod
    def locations():
        visited = len(Place.place_list)
        if visited:
            place_list.append(location)
    
    def __init__(self, name, location):
        self.__name = name
        self.__location = location
        self.__unknown = True

    def __str__(self):
        reply += self.__name + "created." + "\n"
        reply += self.__name + "created." + "\n"
        if self.unknown: 
            reply += self.__name + "located in " + self.location + "\n"
        else:
            reply += self.__name + "\n"
        return reply

    def get_name(self, name):
        return self.__name

    def get_location(self, location):
         return self.__location

class Home(Place):

    def __init__(self, bedrooms, occupancy):
        self.bedrooms = bedrooms
        self.occupancy = occupancy

    def __str__(self):
        reply += self.__name + ", " + "located in " + self.__location + self.__unknown + ".\n"
        + "\t" + "This house has " + str(self.bedrooms) + " bedrooms, of which " + str(self.occupancy) + " are occupied."

        return reply
    
class City(Place):

    def __init__(self, population, mayor):
        self.population = population
        self.mayor = mayor

    def __str__(self):
        reply += self.__name + ", located in " + self.__location + self.__unknown + ".\n"
        + "\t" + "This city has " + str(self.population) + " residents, and the mayor is " + self.mayor + "."
        
        return reply
    
    @staticmethod
    def visit():
        visited2 += "That means... " + "You visit " + self.__name + "." + "\n"
        if self.__name in self.__location:
            print("You visit " + self.__name)
            return visited2
            print(self.__location + "has already been visited.")

    @staticmethod
    def is_located_in():
        self.locatedin = True
        if self.__name in self.__location:
            reply += "True or False, " + self.__name + "is located in " + self.__location + ":" + self.locatedin
        else:
            reply += "True or False, " + self.__name + "is located in " + self.__location + ":" + not(self.locatedin)
            

        return reply
