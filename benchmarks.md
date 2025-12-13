## Benchmarks Summary: YOLO Fine-Tuning Iterations

This table summarizes the key hyperparameters and the final performance metrics for each successful model version. The metrics are focused on the difficult detection of `buffalo` and `camel` classes.

| Version | Base Model | Epochs (Max) | Patience | Batch/Workers | Key Hyperparameters | $\mathrm{mAP50}$ (Local Peak) | $\mathrm{mAP50-95}$ (Local Peak) |
| :---: | :---: | :---: | :---: | :---: | :--- | :---: | :---: |
| **v1** | `yolo11s.pt` | 30 | N/A | 8 / 8 | Default settings | No meaningful metrics | No meaningful metrics |
| **v2** | N/A | N/A | N/A | N/A | Testing parameters | N/A | N/A |
| **v3** | N/A | 40 | 5 | 8 / 10 | Default optimizer | 0.8313 | 0.6066 |
| **v4** | N/A | N/A | N/A | N/A | Learning Rate attempt (Failed) | 0.8313 | 0.6066 |
| **v5** | N/A | 40 | 10 | 8 / 10 | **AdamW, LR=$10^{-3}$, $LR_f=10^{-4}$** | 0.8395 | 0.6491 |
| **v6** | N/A | 35 | 5 | 8 / 10 | Continuation of v5 strategy | **0.8392** | **0.6565** |

### Key Observations and Performance Analysis

#### Hardware and Time Constraints
All runs were executed on an **Nvidia RTX 2050** with an approximate training time of **2 minutes per epoch**. This constraint influenced the decision to optimize run efficiency in later versions.

#### Hyperparameter Evolution

* **v3** established the initial strong baseline with $\mathrm{mAP50-95}$ at $0.6066$.
* **v4** failed to manually set the learning rate, reinforcing the need to explicitly define the optimizer.
* **v5** implemented the critical fine-tuning strategy:
    * **Optimizer:** Switched to `AdamW`.
    * **Learning Rate:** Reduced initial LR to $0.001$ and final LR to $0.0001$.
    * **Result:** This change led to a substantial jump in **localization precision** ($\mathrm{mAP50-95}$ increased from $0.6066$ to $0.6491$), confirming the benefits of a slower, more stable training process.
* **v6** fine-tuned the stopping criteria:
    * **Patience:** Reduced to 5 (from 10 in v5).
    * **Epochs:** Reduced to 35 (from 40 in v5).
    * **Result:** Achieved the **overall best localization score** of $\mathbf{0.6565}$ in $\mathrm{mAP50-95}$, demonstrating successful convergence control.

#### Local vs. W&B Metrics

As noted, the differences observed between local (raw, instantaneous peak) and W&B (potentially smoothed or summarized) metrics are expected. The local peak metrics from **v6** represent the best performing checkpoint (likely the one saved as `best.pt`):

| Metric | v6 Local Peak | v6 W&B Logged |
| :--- | :---: | :---: |
| $\mathrm{mAP50}$ | 0.8392 | 0.84335 |
| $\mathrm{mAP50-95}$ | **0.6565** | 0.65193 |
| Precision | 0.8496 | 0.83696 |
| Recall | 0.7992 | 0.80574 |

The local $\mathrm{mAP50-95}$ of $\mathbf{0.6565}$ is the highest measured score for precise localization.
