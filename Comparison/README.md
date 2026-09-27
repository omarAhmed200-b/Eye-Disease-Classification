# Model comparison

The [summary](model_summary.csv), [per-class table](per_class_comparison.csv), [headline graph](accuracy_macro_f1.png), [per-class F1 graph](per_class_f1.png), and [training curves](training_curves.png) use only recovered records.

The Custom CNN test report and historical ResNet18 test report both contain 2,368 samples, but their per-class supports differ. They therefore represent different split membership and must not be interpreted as a controlled comparison. ResNet18 has higher recorded no-TTA accuracy (0.5861 vs 0.5785) and macro-F1 (0.4965 vs 0.3571), but this does not prove it outperformed the Custom CNN on an identical test set.

## Class imbalance

Both records show weaker minority-class behavior. The Custom CNN has F1=0 for AMD and Hypertension; the historical ResNet18 report improves those to 0.1463 and 0.2857, respectively, but on different supports. “Others” remains weak for both. Balanced sampling/augmentation is recorded in the selected Custom CNN checkpoint, while the reconstructed ResNet18 workflow uses class weighting.

## Speed versus accuracy

No measured latency or throughput was recovered for either model. ResNet18's higher recorded macro-F1 favors it on accuracy, while the smaller custom architecture may plausibly be faster; without matched hardware, preprocessing, batch size, and timings, no deployment-speed winner can be claimed.

## Per-class recorded F1 and support

| Class | Custom F1 | Custom support | ResNet18 F1 | ResNet18 support |
|---|---:|---:|---:|---:|
| AMD | 0.0000 | 44 | 0.1463 | 54 |
| Cataract | 0.3614 | 70 | 0.5695 | 68 |
| Diabetic Retinopathy | 0.6550 | 785 | 0.6861 | 824 |
| Glaucoma | 0.5099 | 221 | 0.5805 | 186 |
| Hypertension | 0.0000 | 24 | 0.2857 | 18 |
| Myopia | 0.5172 | 66 | 0.7581 | 58 |
| Normal | 0.6446 | 946 | 0.6843 | 940 |
| Others | 0.1685 | 212 | 0.2617 | 220 |

The unequal supports are direct evidence that this is not an identical-test-set comparison.
