import gym
from gym import Env
from gym.spaces import Discrete, Box
from gym import spaces
from gym.spaces import MultiDiscrete
import numpy as np
from numpy import int8

# Checks if input is inside of grid, if inside grid, inverts light at input. Alerts user if input is outside of grid
def press_in_range(x,y, grid_dimension):
    if not (0 <= x < grid_dimension):
        print(f'Invalid X input, {x} out of range')
        return False
    if not (0 <= y < grid_dimension):
        print(f'Invalid Y input, {y} out of range')
        return False
    return True

# Checks if input is inside of grid, if inside grid, inverts light at input
def side_in_range(x,y, grid_dimension):
    if not (0 <= x < grid_dimension):
        return False
    if not (0 <= y < grid_dimension):
        return False
    return True

def light_press(x,y, light_matrix, grid_dimension):

    # Check if input is inside of grid, if inside grid, inverts light at input
    # If input is not insde grid, returns without affecting the lights
    if not press_in_range(x,y, grid_dimension):
        return
    light_matrix[x][y] = not light_matrix[x][y]

    # Check left of input
    if not side_in_range(x, y-1, grid_dimension):
        pass
    else:
        light_matrix[x][y-1] = not light_matrix[x][y-1]

    # Check right of input
    if not side_in_range(x, y+1, grid_dimension):
        pass
    else:
        light_matrix[x][y+1] = not light_matrix[x][y+1]

    # Check over input
    if not side_in_range(x+1, y, grid_dimension):
        pass
    else:
        light_matrix[x+1][y] = not light_matrix[x+1][y]

    # Check below input
    if not side_in_range(x-1, y, grid_dimension):
        pass
    else:
        light_matrix[x-1][y] = not light_matrix[x-1][y]
    return

light_out = "□"
light_on = "■"

# Prints the light matrix in a readable format
def print_matrix(light_matrix):
    for x in light_matrix:
        for y in x:
            if y:
                print(light_on, end = '')
            else:
                print(light_out, end = '')

        print("")

# Checks if all lights are out, returns true if all lights are out, false if not
def check_if_compleate(light_matrix):
    check_array = []

    for x in light_matrix:
        if (any(x)):
            check_array.append(True)
        else:
            check_array.append(False)
    return not any(check_array)

# Counts the number of lights that are on and returns the number
def light_count(light_matrix):
    i = 0
    for x in light_matrix:
        for y in x:
            if not y:
                i+=1

    return i

# Environment class definition for Lights Out
class LightsOutEnv(Env):
    def __init__(self):
        super(LightsOutEnv, self).__init__()
        self.bord_size = 5
        # Each place on the board is represented by a number, with first field being 1 and last being bord_size^2
        self.action_space = Discrete((self.bord_size**2))
        #self.action_space = MultiDiscrete([self.bord_size, self.bord_size])
        self.observation_space =  gym.spaces.MultiBinary([self.bord_size, self.bord_size])
        #self.observation_space = Box(low=0, high=1, shape=(self.bord_size, self.bord_size))
        #self.state = np.array([[True for i in range(self.bord_size)] for j in range(self.bord_size)], dtype=int8).flatten()
        self.max_steps = 100
        self.last_action = None
        self.last_last_action = None
        self.last_last_last_action = None

    def step(self, action):
        # Translates input to x and y coordinates
        x_cord = action // self.bord_size
        #x_cord = action[0]
        y_cord = action % self.bord_size
        #y_cord = action[1]

        reward = 0

        self.max_steps -= 1

        # Checks how many lights are on before action
        lights_before_action = light_count(self.state)

        # Executes action
        light_press(x_cord, y_cord, self.state, self.bord_size)

        # Checks if all lights are out
        done = check_if_compleate(self.state)


        # If all lights are out, reward is set to 10
        if done:
            reward = 1000
        # If all lights are not out, reward is set to 1 if number of lights is reduced, -1 if number of lights is increased
        else:
            if self.last_action == action:
                reward = -5
            else:
                #reward = 5
                reward =+ light_count(self.state) - lights_before_action
                                
            # termitnate wehn stuck in loop or max steps reached
            if action == self.last_action and self.last_action == self.last_last_action and self.last_last_action == self.last_last_last_action:
                reward = -15
                done = True
            
            if self.max_steps < 0:
                done = True
                reward = -15

            #if lights_before_action < light_count(self.state):
            #    reward = light_count(self.state) - lights_before_action
            #elif self.last_action == action:
            #    reward = -5
            #else:
            #    reward = light_count(self.state)

        self.last_last_last_action = self.last_last_action
        self.last_last_action = self.last_action
        self.last_action = action


        info = {}

        return self.state, reward, done, info

    # Prints the light matrix in a readable format
    def print_table(self):
        print_matrix(self.state)

    # Resets the environment
    def reset(self):
        self.last_action = None
        self.last_last_action = None
        self.last_last_last_action = None
        self.max_steps = 100

        self.state = np.array([[True for i in range(self.bord_size)] for j in range(self.bord_size)], dtype=int8)
        return self.state

