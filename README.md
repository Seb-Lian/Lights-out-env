# Lights-out-env

Enviroment for traning a RL modell to solve the game Lights Out.
The enviroment is written such that the size of the board can be changed by chaning the 'self.bord_size' variable in the init function. The default size is 5x5.

The enviroment is writen such that it can be used with the OpenAI gym library and Stable Baselines 3.
Rewards could use some work, as the current reward system is not very good and makes the modell learn very slowly or not at all.


## Use
To use the enviroment, you just need to install the package and import it.
```python
from lights_out_env import LightsOutEnv
```
The enviroment can then be used like any other OpenAI gym enviroment.
```python
env = LightsOutEnv()
env.reset()
```
## Other files
The training.py file is used to train a modell using Stable Baselines 3.

IKT_460_light_out_test.py is used to test the modell after training.