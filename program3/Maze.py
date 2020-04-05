import numpy

class Node(object):
    
    def __init__(self, wall, qValues = [0], nValues = [0]):

        self.isWall = wall

        if(self.isWall == False):
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
