class Robot(object):
    robot_list = []

    @staticmethod
    def contenders():
        robots = len(Robot.robot_list)
        print("There are", robots, "robots.\n")
        if robots:
            print("Here is a list of them:")
            for robot in Robot.robot_list:
                print(robot)

    def __init__(self, name, weapon, strength):
        print("Robot created!", name, "\n")
        self.name = name
        self.weapon = weapon
        self.strength = strength
        self.online = True
        Robot.robot_list.append(self)

    def __str__(self):
        reply = "-" * 20 + "\n"
        reply += "Fighting Robot\n"
        reply += "Name: " + self.name + "\n"
        reply += "Weapon: " + self.weapon + "\n"
        reply += "Strength: " + str(self.strength) + "\n"
        if self.online:
            reply += "Status: ONLINE\n"
        else:
            reply += "Status: OFFLINE\n"
        reply += "-" * 20 + "\n"
        return reply

#main
Robot.contenders()

r2d2 = Robot("Optimus", "Fists", 10)
c3p0 = Robot("Voltron", "Sword", 10)

Robot.contenders()
