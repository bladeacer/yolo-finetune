from ultralytics import YOLO
from ultralytics import settings

# Run before training
# wandb login

settings.update({"wandb": True,
                 "tensorboard": False})

model = YOLO("yolo11s.pt") 

result = model.train(
    data="yolo-fine-1/data.yaml",
    epochs=40,
    patience=5,
    save_period=1,
    batch=8,
    device="0",
    project='yolo-fine',
    plots=True
)
