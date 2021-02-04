import torch

from environment import CarRacingEnv
from trainer import Trainer

# if gpu is to be used
device = torch.device("cuda") if False else torch.device("cpu")

if __name__ == "__main__":
    hyperparams = {
        'lr': 1e-2,  # Learning rate
        'gamma': 0.99,  # Discount rate
        'log_interval': 1,  # controls how often we log progress
        'num_episodes': 10,  # number of episodes to train on
        'params_path': './params/policy-params.dl'
    }

    x=1 
    while x < 500:
        env = CarRacingEnv(device)
        print(env.reset())
        trainer = Trainer(env, hyperparams)
        trainer.train()
        x +=1 
        print(x)
