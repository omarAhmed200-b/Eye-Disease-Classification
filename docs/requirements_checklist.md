# Assignment requirement checklist

Source: [assignment.pdf](assignment.pdf).

| Requirement | Status | Evidence / limitation |
|---|---|---|
| Explore 11,839 images and splits | Met | [Dataset analysis](../Dataset_Analysis/README.md) and CSV manifests |
| Plot all eight class counts | Met | [Distribution chart](../Dataset_Analysis/class_distribution.png) |
| Show samples from every class | **Missing** | Genuine images were not supplied; none fabricated |
| Address class imbalance | Partially evidenced | Custom checkpoint records balanced sampling/augmentation; reconstructed ResNet18 workflow uses weighted loss |
| Custom CNN from scratch | Partially met | Checkpoint/results recovered; original complete training notebook missing |
| Reasonable Custom CNN convergence | Met from records | [Recorded histories](../Custom_CNN/figures/training_history.png) |
| Fine-tune pretrained model | Met from historical records | [Reconstructed workflow](../ResNet18/notebooks/resnet18_full_reconstructed.ipynb); checkpoint missing |
| Pretrained model outperforms scratch CNN | Not controlled | ResNet18 records are higher, but test supports prove different membership |
| Per-class precision, recall, and F1 for both | Met from records | [Side-by-side CSV](../Comparison/per_class_comparison.csv) and [discussion](../Comparison/README.md) |
| Compare speed and accuracy | Incomplete | Accuracy recorded; inference speed missing for both models |
| Code on GitHub with README | Prepared only | Repository and README ready; not committed or pushed |
| Verified Kaggle notebook links | **Missing** | No Kaggle URLs present; README uses explicit placeholders |

Reconstructed notebooks are labeled and are not evidence that their code produced the historical outputs.
