# Lights-out-env

Enviroment for traning a RL modell to solve the game Lights Out.
The enviroment is written such that the size of the board can be changed by chaning the 'self.bord_size' variable in the init function. The default size is 5x5.

The enviroment is writen such that it can be used with the OpenAI gym library and Stable Baselines 3.
Rewards could use some work, as the current reward system is not very good and makes the modell learn very slowly or not at all.