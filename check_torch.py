import torch
if torch.cuda.is_available():
    print(f"GPU: {torch.cuda.get_device_name()} is available.")
else:
    print("No GPU available. Training will run on CPU.")