# Custom CNN artifacts

This folder contains the recovered Custom CNN checkpoint and recorded results. No retraining was performed.

## Notebook status

- [custom_cnn_reconstructed_artifact_report.ipynb](notebooks/custom_cnn_reconstructed_artifact_report.ipynb) consolidates recovered histories, checkpoint metadata, final metrics, and TTA data. It is **reconstructed**, not the original training notebook.
- The original complete Custom CNN training notebook was not recovered.
- Kaggle URL: `KAGGLE_URL_NOT_RECOVERED — replace with verified URL`.

## Saved artifacts

- [Selected checkpoint](checkpoints/best_custom_cnn.pth), with [SHA-256 record](checkpoints/SHA256SUMS).
- [Load-compatible reconstructed model definition](src/model.py). Stateless layer placement cannot be proven from the checkpoint alone.
- [Training histories](results/training/) and [training graph](figures/training_history.png).
- [Final test metrics](results/final_test/final_test_results.json), [classification report](results/final_test/classification_report.csv), and [confusion matrix](results/final_test/final_confusion_matrix.png).
- [Validation TTA table](results/tta/tta_validation_comparison.csv) and [graph](figures/tta_validation_comparison.png).
- [Recovered split manifests](splits/).

Recorded final test result: accuracy 0.578547 and Macro F1 0.357090 on 2,368 samples without TTA.
