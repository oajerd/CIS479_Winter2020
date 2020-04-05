class Node(object):
    
    def __init__(self, wall, qValues, nValues):

        self.isWall = wall

        self.qNorth = qValues[0]
        self.qEast = qValues[1]
        self.qSouth = qValues[2]
        self.qWest = qValues[3]

        self.nNorth = nValues[0]
        self.nEast = nValues[1]
        self.nSouth = nValues[2]
        self.nWest = nValues[3]

class Map(object):
    def __init__(self, wall_file, goal_file, size_x, size_y):
        self.x = size_x
        self.y = size_y
        self._wall_file = wall_file
        self._goal_file = goal_file
        self.map = [[Node(False, [0.0,0.0,0.0,0.0],[0,0,0,0]) for i in range(size_x)] for j in range(size_y)]

        self.setup_map()

    def setup_map(self):

        wall_file = open(self._wall_file, "r")

        for line in wall_file:
            indicies = line.split(",")
            self.map[int(indicies[0])][int(indicies[1])].isWall = True
            
        goal_file = open(self._goal_file, "r")

        line = goal_file.readline()
        indicies = line.split(",")
        self.map[int(indicies[0])][int(indicies[1])].qNorth = 100.0
        self.map[int(indicies[0])][int(indicies[1])].qSouth = 100.0
        self.map[int(indicies[0])][int(indicies[1])].qEast = 100.0
        self.map[int(indicies[0])][int(indicies[1])].qWest = 100.0

        line = goal_file.readline()
        indicies = line.split(",")
        self.map[int(indicies[0])][int(indicies[1])].qNorth = -100.0
        self.map[int(indicies[0])][int(indicies[1])].qSouth = -100.0
        self.map[int(indicies[0])][int(indicies[1])].qEast = -100.0
        self.map[int(indicies[0])][int(indicies[1])].qWest = -100.0



    def printMapQvalues(self):
        for row in self.map:
            top = ""
            middle = ""
            bottom = ""
            for item in row:
                if item.isWall:
                    middle += "####"
                else:
                    top += "    " + item.qNorth.__str__()
                    middle += item.qWest.__str__() + "   " + item.qEast.__str__()
                    bottom += "     " + item.qSouth.__str__()

            print(top)
            print(middle)
            print(bottom)
            print()

    def printMapNvalues(self):
        for row in self.map:
            top = ""
            middle = ""
            bottom = ""
            for item in row:
                if item.isWall:
                    middle += "####"
                else:
                    top += "    " + item.nNorth.__str__()
                    middle += item.nWest.__str__() + "   " + item.nEast.__str__()
                    bottom += "     " + item.nSouth.__str__()

            print(top)
            print(middle)
            print(bottom)
            print()

    def print_optimal_path(self):
        for x in range(0, self.x):
            line_str = ""
            for y in range(0, self.y):
                if self.map[x][y].isWall == False:
                    q_max = 0.0
                    if self.map[x][y].qNorth > q_max:
                        q_max = self.map[x][y].qNorth
                        action = "n"
                    if self.map[x][y].qSouth > q_max:
                        q_max = self.map[x][y].qSouth
                        action = "s"
                    if self.map[x][y].qEast > q_max:
                        q_max = self.map[x][y].qEast
                        action = "e"
                    if self.map[x][y].qWest > q_max:
                        q_max = self.map[x][y].qWest
                        action = "w"

                    if action == "n":
                        line_str += "^^^^    "
                    if action == "e":
                        line_str += ">>>>    "
                    if action == "s":
                        line_str += "vvvv    "
                    if action == "w":
                        line_str += "<<<<    "
                else:
                    line_str += "####    "
            print(line_str)

                

