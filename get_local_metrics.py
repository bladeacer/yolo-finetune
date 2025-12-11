from ultralytics import YOLO

train_ver = 3

model = YOLO(f"yolo-fine/train{train_ver}/weights/best.pt")

validation_results = model.val(data="yolo-fine-1/data.yaml", device="0")

print("\n--- Key Metrics ---")
print(f"Overall mAP50 (map50): {validation_results.box.map50:.4f}")
print(f"Overall mAP50-95 (map): {validation_results.box.map:.4f}")
print(f"Mean Precision (mp): {validation_results.box.mp:.4f}")
print(f"Mean Recall (mr): {validation_results.box.mr:.4f}")
