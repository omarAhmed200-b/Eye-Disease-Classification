# Eye Disease Classification — ResNet18 (Kaggle / PyTorch)

**Status: reconstructed training notebook + recorded historical results; original checkpoint NOT recovered.** This folder documents the pretrained-model portion of the combined assignment. The separate Custom CNN artifacts are available in [`../Custom_CNN/`](../Custom_CNN/). Original inference timing was not recorded.

## Contents

- `notebooks/resnet18_full_reconstructed.ipynb`: end-to-end **reconstructed** Kaggle workflow, including new group-aware splits, training, checkpointing, per-class reports, inference timing, optional validation TTA, and downloadable outputs archive.
- `source_notebooks/`: the recovered original Kaggle *fragments* (data import and TTA report only).
- `results/`: **historical console outputs**, manually transcribed from the previous Kaggle run. These are not a newly reproduced run.
- `figures/historic_validation_progress.png`: historical metrics visualization.
- `models/README.md`: checkpoint recovery limitation and instructions.
- `requirements.txt`: notebook dependencies.

## Historical data and model setup

11,839 images, eight classes: AMD, Cataract, Diabetic Retinopathy, Glaucoma, Hypertension, Myopia, Normal, Others. Source datasets: ODIR5K, APTOS2019, ACRIMA, ORIGA. Historic group-aware (ODIR patient ID) split: **8,287 train / 1,184 validation / 2,368 test**. Historic split **CSVs were not recovered**; the reconstructed notebook generates a new split unless the original CSVs are supplied. Independence of patients in non-ODIR sources and cross-dataset duplicate absence was not verified.

ResNet18 ImageNet pretrained; first train FC with backbone frozen (5 epochs), then fine-tune layer4 + FC (5 epochs), followed by reweighting with square-root inverse class frequencies (5 epochs). Adam, batch size 32, images resized to 224×224, class-weighted cross-entropy. Model selection: **validation Macro F1**. Training and validation use different transforms; the held-out test is never used to update weights in the reconstructed workflow.

## Historical metrics (previous run; checkpoint missing)

| Stage / inference | Split | Accuracy | Macro F1 |
|---|---|---:|---:|
| Frozen-backbone FC only — best epoch | Validation | 0.5329 | 0.4213 |
| Layer4 fine-tuning — best epoch | Validation | 0.5270 | 0.4693 |
| sqrt-reweighted fine-tuning — best epoch | Validation | 0.5929 | 0.5057 |
| Original inference | Test | 0.5861 | 0.4965 |
| Flip TTA (2 views) | Validation | 0.5988 | 0.5175 |
| 4-view TTA | Validation | 0.6132 | 0.5177 |
| 8-view TTA | Validation | 0.6360 | 0.5268 |
| 4-view TTA — exploratory retest | Test | 0.6035 | 0.5012 |

**Important:** TTA was explored on validation *after* the initial test had been seen. Therefore the 4-view retest is exploratory and does not count as a fresh independent evaluation of a newly fixed method. No test result exists for 8-view TTA. Historical TTA results are not proof of clinical generalization.

The original test per-class results are in `results/historic_test_classification_report.csv`; e.g., AMD F1 0.1463, Hypertension F1 0.2857 (18 images), and Others F1 0.2617. The legacy validation set had only 8 Hypertension examples, all missed by the model. Distinct dataset sources showed large shifts in recall for the same label (notably DR and Normal). A trained fundus model with these results is **not a clinical diagnostic system**.

## Run on Kaggle

1. Create a GPU Kaggle Notebook, import `notebooks/resnet18_full_reconstructed.ipynb`, enable Internet if pretrained weights are not cached.
2. Attach a legally accessible copy of the dataset containing `metadata.csv` and `images/` via **Add Input**, OR supply the user's original ZIP at `/kaggle/working/eye_dataset.zip`. Change `DATA_DIR`/`DATA_ZIP` in cell 2 as necessary. The ~4-GB original dataset is **not** included here and should **not** be committed to GitHub.
3. Run cells top-to-bottom. New split files will be created inside `/kaggle/working/eye_disease_outputs/splits_v2/` unless your *original* split CSVs are supplied. **New results will not necessarily match the historical results.**
4. Inspect validation metrics to choose a checkpoint and TTA policy **before** the held-out test cell. If resuming, inspect existing checkpoint files; the training function refuses to overwrite them silently.
5. At the end, run the final backup cell. **Download `/kaggle/working/eye_disease_training_outputs.zip` while the session is still active. Verify the `.pth` appears inside it before ending the session.** Separately save the Notebook `.ipynb` to your computer. A Kaggle Quick Save of code is not sufficient proof that `/kaggle/working` files are preserved.

## Dataset / source handling

The historic original grouped split was not among the recovered notebook fragments, so this repo supplies a reproducible *new* group-aware split method. It parses ODIR patient IDs from image filenames, and groups other sources per filename where patient identifiers are not established. Cross-source duplicate detection and full patient independence require separate auditing. Do not report the historic metrics as metrics from this newly generated split.

## Submission status / remaining tasks

- ✅ Reconstructed pretrained ResNet18 training and historical results documentation.
- ✅ Historical per-class test metrics and validation TTA comparison, explicitly labelled.
- ⚠️ Original checkpoints and original split CSVs missing; reproduction requires a new run.
- ⚠️ Original inference speed not recorded; code included to measure it in a new run.
- ✅ Separate Custom CNN checkpoint and recorded metrics are included in [`../Custom_CNN/`](../Custom_CNN/), with its missing original training notebook disclosed.

## Large files

The repository-level `.gitignore` excludes datasets and unselected `.pth` checkpoints. Do not upload the dataset or claim results from unexecuted code.
