# YOLO Finetune

<p align="center">
    <a href="https://universe.roboflow.com/stuff-avvl2/yolo-fine-y444l">
        <img src="https://app.roboflow.com/images/download-dataset-badge.svg"></img>
    </a>
    <a href="https://huggingface.co/bladeacer/yolo-fine/tree/main">
        OpenVino Model
    </a>
    <a href="https://huggingface.co/spaces/IT3103-2025S2/232343X">
        HuggingFace Instance
    </a>
</p>

Finetuning YOLO v11 on `buffalo` and `camel` image data.

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

## Training the model

```bash
wandb login
python train_model.py
```

## Benchmarks
See [Benchmarks file](./benchmarks.md).

## Credits

Data labelling done on Roboflow. Benchmarks with wandb.

[Water Buffalo dataset](https://images.cv/dataset/water-buffalo-image-classification-dataset)

[Camel dataset](https://images.cv/dataset/camel-image-classification-dataset)

Use Roboflow CLI to upload data. The [upload_dataset](./upload_dataset.sh) is a helper script for this.

[Roboflow project link](https://universe.roboflow.com/stuff-avvl2/yolo-fine-y444l)

[Stock buffalo footage](https://www.pexels.com/video/close-up-video-of-a-carabao-in-the-farm-5795227/)

[Stock camel image](https://unsplash.com/photos/brown-camels-on-desert-during-daytime-zFWfrZ4rmcc)

