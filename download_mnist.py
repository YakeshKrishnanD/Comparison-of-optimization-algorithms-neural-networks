import os
from torchvision import datasets

# Define where you want to save the dataset locally
data_path = './data'

print("Downloading MNIST dataset directly to your local system...")

# This downloads both training and test sets and creates the 'data' directory automatically
train_dataset = datasets.MNIST(root=data_path, train=True, download=True)
test_dataset = datasets.MNIST(root=data_path, train=False, download=True)

print(f"Success! Dataset downloaded and saved to: {os.path.abspath(data_path)}")