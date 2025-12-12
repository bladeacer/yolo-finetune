import multiprocessing
import sys
from ultralytics import YOLO
from ultralytics import settings
import os

LOG_FILE = "train_model.log"
MAX_WORKERS = max(1, multiprocessing.cpu_count() - 2)
BATCH_SETTING = 8
LR0 = 0.001 
LRF = 0.0001
EPOCHS = 35
PATIENCE = 5
DET = False

# Custom Class to output to stdout + log file
class Tee(object):
    """Duplicates stdout output to both a terminal stream and a file."""
    def __init__(self, filename, mode="a", stream=sys.stdout):
        self.terminal = stream
        self.log_file = open(filename, mode)

    def write(self, message):
        self.terminal.write(message)
        self.log_file.write(message)

    def flush(self):
        self.terminal.flush()
        self.log_file.flush()

    def __enter__(self):
        self.original_stdout = sys.stdout
        sys.stdout = self
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self.original_stdout
        self.log_file.close()

settings.update({
    "wandb": True,
    "tensorboard": False,
})

print(f"Starting YOLOv11 training. Output will be saved to {LOG_FILE} and console.")

with Tee(LOG_FILE, mode='a') as t:
    print("-" * 50)
    print(f"Training session started at: {os.uname().nodename}")
    print(f"Using {MAX_WORKERS} multiprocessing workers (workers argument).")
    print(f"Using batch={BATCH_SETTING}.")
    print("-" * 50)
    
    try:
        model = YOLO("yolo11s.pt")

        result = model.train(
            data="yolo-fine-1/data.yaml",
            epochs=EPOCHS,
            patience=PATIENCE,
            save_period=1,
            batch=BATCH_SETTING,
            workers=MAX_WORKERS,
            device="0",
            project='yolo-fine',
            plots=True,
            optimizer="AdamW",
            lr0=LR0,
            lrf=LRF,
            deterministic=DET
        )

    except Exception as e:
        print(f"\n[ERROR] An exception occurred during training: {e}", file=sys.stderr)

print(f"Training finished. Full log available in {LOG_FILE}.")
