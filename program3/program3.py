from Maze import Node
from Maze import Map
from random import random
from random import seed

class QLearning(object):
    def __init__(self, lamda, maze_map):
        self._lambda = lamda
        self.current_location = [0,0]
        self.map = maze_map

    def run_cycle(self):
        return

    def determine_action(self, node):
        seed(1)
        action_prob = random()
        action = ""

        if action_prob <= 0.95:
            q_max = 0.0
            if node.qNorth > q_max:
                q_max = node.qNorth
                action = "n"
            if node.qSouth > q_max:
                q_max = node.qSouth
                action = "s"
            if node.qEast > q_max:
                q_max = node.qEast
                action = "e"
            if node.qWest > q_max:
                q_max = node.qWest
                action = "w"
        else:
            rand_action = random.randint(1,4)
            if rand_action == 1:
                action = "n"
            elif rand_action == 2:
                action = "e"
            elif rand_action == 3:
                action = "s"
            elif rand_action == 4:
                action = "w"

        return action

    def calculate_q(self, current, reward, action, next):
        updated_q = 0
        current_q = 0
        current_n = 0
        q_next_max = 0.0
        reward = 0

        if action == "n":
            current_q = current.qNorth
            current_n = current.nNorth
            reward = -1.0
        if action == "e":
            current_q = current.qEast
            current_n = current.nEast
            reward = -2.0
        if action == "s":
            current_q = current.qSouth
            current_n = current.nSouth
            reward = -3.0
        if action == "w":
            current_q = current.qWest
            current_n = current.nWest
            reward = -2.0

        if next.qNorth > q_next_max:
            q_max = next.qNorth
        if next.qSouth > q_next_max:
            q_max = next.qSouth
        if next.qEast > q_next_max:
            q_max = next.qEast
        if next.qWest > q_next_max:
            q_max = next.qWest

        updated_q = current_q + ((1.0/float(current_n)) * (reward + (self._lambda * q_max) - current_q))

        return updated_q

    def calculate_n(self, current, action):
        n = 0

        if action == "n":
            n = current.nNorth + 1
        if action == "e":
            n = current.nEast + 1
        if action == "s":
            n = current.nSouth + 1
        if action == "w":
            n = current.nWest + 1
        
        return n

    def calculate_next_location(self, current, x, y):
        action = self.determine_action(current)
        next_location = [0,0]

        drift_prob = random()
        drift = "none"

        if drift_prob >= 0.90 and drift_prob < 0.95:
            drift = "right"
        elif drift_prob >= 0.95:
            drift = "left"

        if drift == "none":
            if action == "n":
                next_location = [x, y+1]
            if action == "e":
                next_location = [x+1, y]
            if action == "s":
                next_location = [x, y-1]
            if action == "w":
                next_location = [x-1, y]

        elif drift == "right":
            if action == "n":
                next_location = [x+1, y] # move east instead
            if action == "e":
                next_location = [x, y-1] # move south instead
            if action == "s":
                next_location = [x-1, y] # move west instead
            if action == "w":
                next_location = [x, y+1] # move north instead
        elif drift == "left":
            if action == "n":
                next_location = [x-1, y] # move west instead
            if action == "e":
                next_location = [x, y+1] # move north instead
            if action == "s":
                next_location = [x+1, y] # move east instead
            if action == "w":
                next_location = [x, y-1] # move south instead

        return next_location


newMap = Map("walls.txt", "goals.txt", 7, 7)