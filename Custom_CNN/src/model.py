"""Load-compatible model definition recovered from the saved checkpoint.

The parameterized layer names and shapes exactly match the checkpoint. ReLU,
pooling, and dropout placements are reconstructed because those layers do not
store tensors in a PyTorch state_dict; see README.md for this limitation.
"""

from pathlib import Path

import torch
from torch import nn


class CustomCNN(nn.Module):
    """Four-block convolutional classifier for eight eye-disease classes."""

    def __init__(self, num_classes: int = 8) -> None:
        super().__init__()
        self.block1 = self._block(3, 32)
        self.block2 = self._block(32, 64)
        self.block3 = self._block(64, 128)
        self.block4 = self._block(128, 256)
        self.pool = nn.AdaptiveAvgPool2d((1, 1))
        self.classifier = nn.Sequential(
            nn.Dropout(0.5),
            nn.Linear(256, 128),
            nn.ReLU(inplace=True),
            nn.Dropout(0.3),
            nn.Linear(128, num_classes),
        )

    @staticmethod
    def _block(in_channels: int, out_channels: int) -> nn.Sequential:
        return nn.Sequential(
            nn.Conv2d(in_channels, out_channels, 3, padding=1, bias=False),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True),
            nn.Conv2d(out_channels, out_channels, 3, padding=1, bias=False),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        for block in (self.block1, self.block2, self.block3, self.block4):
            x = block(x)
        x = self.pool(x).flatten(1)
        return self.classifier(x)


def load_checkpoint(path: str | Path, device: str | torch.device = "cpu"):
    """Load the recovered checkpoint safely and return model, metadata."""
    path = Path(path)
    try:
        checkpoint = torch.load(path, map_location=device, weights_only=True)
    except TypeError:  # PyTorch versions predating weights_only
        checkpoint = torch.load(path, map_location=device)

    classes = checkpoint.get("classes", [])
    model = CustomCNN(num_classes=len(classes) or 8).to(device)
    model.load_state_dict(checkpoint["model_state_dict"], strict=True)
    model.eval()
    return model, checkpoint
