# Import routines

import numpy as np
import math
import random
import collections
from itertools import product

# Defining hyperparameters
m = 5 # number of cities, ranges from 1 ..... m
t = 24 # number of hours, ranges from 0 .... t-1
d = 7  # number of days, ranges from 0 ... d-1
C = 5 # Per hour fuel and other costs
R = 9 # per hour revenue from a passenger


class CabDriver():

    def __init__(self):
        """initialise your state and define your action space and state space"""
        self.action_space = [val for val in list(product(range(0,m),repeat = 2)) if val[0] != val[1]]
        self.state_space = list(product(range(0,m),range(0,t),range(0,d)))
        self.state_init = random.choice(self.state_space)
        # Start the first round
       # self.reset()


    ## Encoding state (or state-action) for NN input

    def state_encod_arch1(self, state):
        """convert the state into a vector so that it can be fed to the NN. This method converts a given state into a vector format. Hint: The vector is of size m + t + d."""
        state_encod = np.zeros((m + t + d), dtype = np.int)
        index_to_be_high = [state[0],m+state[1],m+t+state[2]]
        for ind in index_to_be_high:
            state_encod[ind] = 1
        return state_encod


    #Use this function if you are using architecture-2 
    def state_encod_arch2(self, state, action):
        """convert the (state-action) into a vector so that it can be fed to the NN. This method converts a given state-action pair into a vector format. Hint: The vector is of size m + t + d + m + m."""
        state_encod = np.zeros((3*m + t + d), dtype = np.int)
        index_to_be_high = [state[0],m+state[1],m+t+state[2],m+t+d+action[0],m+t+d+m+action[1]]
        for ind in index_to_be_high:
            state_encod[ind] = 1
        return state_encod


    ## Getting number of requests

    def requests(self, state):
        """Determining the number of requests basis the location. 
        Use the table specified in the MDP and complete for rest of the locations"""
        location = state[0]
        if location == 0:
            requests = np.random.poisson(2)
        if location == 1:
            requests = np.random.poisson(12)
        if location == 2:
            requests = np.random.poisson(4)
        if location == 3:
            requests = np.random.poisson(7)
        if location == 4:
            requests = np.random.poisson(8)

        if requests >15:
            requests =15

        possible_actions_index = random.sample(range(0, (m-1)*m), requests) # (0,0) is not considered as customer request
        actions = [self.action_space[i] for i in possible_actions_index]
        
        actions.append((0,0))
        possible_actions_index.append(20)

        return possible_actions_index,actions   



    def step(self, state, action_index, Time_matrix):              # take care of terminal state
        """Takes in state, action and Time-matrix and returns the reward"""
        if action_index == 20:
            #print("state = {0} {1} {2}, action = {3}".format(state[0],state[1],state[2], action_index))
            total_time = 1
            reward = -C
            action = [0,state[0]]
        else:
            action = self.action_space[action_index]
            #print("state = {0} {1} {2}, action = {3} {4}".format(state[0],state[1],state[2],action[0],action[1]))
            time_start_dest = Time_matrix[action[0]][action[1]][state[1]][state[2]]
            time_curr_start = Time_matrix[state[0]][action[0]][state[1]][state[2]]
            total_time = int(time_curr_start + time_start_dest)
            reward = R * (time_start_dest) - C * (total_time)
        next_state = self.next_state_func(state, action, total_time)
        
        return (next_state, reward, total_time)



    def next_state_func(self, state, action, total_time):
        """Takes state and action as input and returns next state"""
        fin_dest = action[1]
        fin_time = total_time + state[1]
        if fin_time <= t-1:
            fin_day = state[2]
        else:
            fin_time = fin_time - t
            fin_day = state[2] + 1
            
        if fin_day > 6:
            fin_day = 0
            
        return (fin_dest, fin_time, fin_day)



    def reset(self):
        return self.action_space, self.state_space, self.state_init
