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

from light_out_env_positive_board_compleation import LightsOutEnv

env = LightsOutEnv()

# ce(env, warn=False, skip_render_check=True)

# gym.utils.env_checker.check_env(env, warn=True, skip_render_check=True)


TIMESTEPS = 50000

iters = 0

models_dir = f"models/{int(time.time())}/"
logdir = f"logs/{int(time.time())}/"	

if not os.path.exists(models_dir):
	os.makedirs(models_dir)

if not os.path.exists(logdir):
	os.makedirs(logdir)

model = PPO("MlpPolicy", env, verbose=1, tensorboard_log=logdir)
info = env.reset()
obs = env.reset()

while True:
	iters += 1
	model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name=f"PPO")
	model.save(f"{models_dir}/{TIMESTEPS*iters}")