# YOLO Finetune

<p align="center">
    <a href="https://universe.roboflow.com/stuff-avvl2/yolo-fine-y444l">
        <img src="https://app.roboflow.com/images/download-dataset-badge.svg"></img>
    </a>
    <a href="https://universe.roboflow.com/stuff-avvl2/yolo-fine-y444l/model/">
        <img src="https://app.roboflow.com/images/try-model-badge.svg"></img>
    </a>
</p>

Finetune YOLO v11 on `buffalo` and `camel` image data.

## Setup

Run the setup script to create a new conda environment, or use `venv`.

```bash
chmod +x setup.py
./setup.py
conda activate yolo-fine
jupyter lab
# Navigate and open analysis.ipynb
```

This script assumes the use of conda and uv.

Installed dependencies are in the [requirements file](requirements.txt).

## Check GPU support

You can run `check_torch.py` to check if your device has GPU supprt for PyTorch.

```bash
python check_torch.py
```

## Credits

Data labelling done on Roboflow. Benchmarks with wandb.

[Water Buffalo dataset](https://images.cv/dataset/water-buffalo-image-classification-dataset)

[Camel dataset](https://images.cv/dataset/camel-image-classification-dataset)

Use Roboflow CLI to upload data. The [upload_dataset](./upload_dataset.sh) is a helper script for this.

[Roboflow project link](https://universe.roboflow.com/stuff-avvl2/yolo-fine-y444l)