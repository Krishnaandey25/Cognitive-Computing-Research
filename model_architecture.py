import torch.nn as nn

class CognitiveNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer = nn.Linear(128, 64)

    def forward(self, x):
        return self.layer(x)

print('Cognitive Model Initialized')