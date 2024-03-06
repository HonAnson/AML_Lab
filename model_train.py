import torch
from torch import nn



class baby_model(nn.Module):
    def __init__(self, numberclasses = 2):
        super(baby_model, self).__init__()

        self.features = nn.Sequential(
            nn.MaxPool2d()



        )