from gym import Env
from gym.spaces import Discrete, Box
from gym import spaces
from gym.spaces import MultiDiscrete
import numpy as np
from numpy import int8
import random
from stable_baselines3 import A2C, PPO, DQN
from stable_baselines3.common.env_checker import check_env as ce
import time
import os

from light_out_env import LightsOutEnv

env = LightsOutEnv()


TIMESTEPS = 100000

iters = 0

model = PPO("MlpPolicy", env, verbose=1)
info = env.reset()
obs = env.reset()

# print(env.action_space.sample())

#for i in range(1000):
#    os.system('clear')
#    print(f"Step: {i}")
#    action = np.random.randint(1, 25)
#    observation, reward, terminated, info = env.step(action)
#    print(reward)
#    env.print_table()
#    time.sleep(0.1)
#    if terminated:
#       obs, info = env.reset()

success = False
blarg = True

model = PPO.load("models/1685625557/100000.zip")

while True:

    env.reset()
    i = 0
    blarg = True
    while blarg:
        os.system('clear')
        print(f"Step: {i}")
        action, _states = model.predict(obs, deterministic=False)
        # action = np.random.randint(0, 24)
        # time.sleep(0.25)
        print(f"Action: {action}")
        obs, reward, terminated, info = env.step(action)
        print(f"Reward: {reward}")
        #print(obs)
        env.print_table()
        time.sleep(0.25)
        i += 1
        if terminated:
            obs = env.reset()
            if reward == 1000:
                print("Success!")
                success = True
            else:
                print("Failure!")
            i = 0
            blarg = False
    if success:
        break   
