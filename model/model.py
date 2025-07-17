import torch
import torch.nn as nn

class modelGame(nn.Module):
    def __init__(self):

        super().__init__()

        self.model=nn.Sequential(
            nn.Linear(9,128),
            nn.ReLU(),
            nn.Linear(128,64),
            nn.ReLU(),
            nn.Linear(64,32),
            nn.ReLU(),
            nn.Linear(32,9)
        )

    def forward(self,x):
        return self.model(x)