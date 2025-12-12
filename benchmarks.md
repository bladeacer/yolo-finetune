## Benchmarks

These are listed in order of iteration.

All training is done on an Nvidia RTX 2050, it does not support CUDA but runs
reasonably quick (2:14 per epoch).

Only modified hyperparameters are mentioned for later versions.

Hyperparameters which are not specified remained unchanged, or are used with
their default values.

Do note that these metrics are for uncommon `buffalo` and `camel` data classes.

Note: Local metrics are based on the best epoch, wandb's are averaged across the epochs.

### v1

Finetuned on: `yolo11s.pt`

Epochs: 30

Batch size: 8

Worker size: 8

#### v1 Metrics: Local
- Overall mAP50 (map50): 0.8506
- Overall mAP50-95 (map): 0.6483
- Mean Precision (mp): 0.8611
- Mean Recall (mr): 0.7792

### v2

Was testing parameters, no meaningful output.

### v3

Epochs: 40

Patience: 5

Worker size: 10

#### v3 Metrics: Local

- Overall mAP50 (map50): 0.8313
- Overall mAP50-95 (map): 0.6066
- Mean Precision (mp): 0.7995
- Mean Recall (mr): 0.7800

#### v3 Metrics: wandb

- Overall mAP50 (B): 0.82634
- Overall mAP50-95 (B): 0.6066
- Mean Precision (B): 0.79927
- Mean Recall (B): 0.80221

### v4

Learning Rate: 0.001 (failed)

#### v4 Metrics: Local

Same as v3.

#### v4 Metrics: wandb

Same as v3.

Did not force learning rate setting change.

### v5

Learning Rate: 0.001

Epochs: 40

Patience: 10

Optimiser: AdamW

Initial Learning Rate: 0.001

Final Learning Rate: 0.0001

Deterministic: False

#### v5 Metrics: Local

- Overall mAP50 (map50): 0.8395
- Overall mAP50-95 (map): 0.6491
- Mean Precision (mp): 0.8280
- Mean Recall (mr): 0.7987

Improved on all fronts slightly compared to v3.

#### v5 Metrics: wandb

- Overall mAP50 (B): 0.6139
- Overall mAP50-95 (B): 0.7934
- Mean Precision (B): 0.82682
- Mean Recall (B): 0.77608

Better mAP50-95, Precision but worse Recall and mAP50.

### v6

Epochs: 35

Patience: 5
