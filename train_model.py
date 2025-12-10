from ultralytics import YOLO
from ultralytics import settings

settings.update({"wandb": True,
                 "tensorboard": False})

model = YOLO("yolo11s.pt") 

result = model.train(
    data="yolo-fine-1/data.yaml",
    epochs=30,
    save_period=1,
    batch=8,
    device="0",
    project='yolo-fine',
    plots=True
)