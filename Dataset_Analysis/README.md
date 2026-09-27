# Dataset analysis

The recovered Custom CNN manifests contain 11,839 labeled rows: 8,287 train, 1,184 validation, and 2,368 test. They cover ODIR5K, APTOS2019, ACRIMA, and ORIGA.

[Class counts](class_distribution.csv), [class-distribution chart](class_distribution.png), [split counts](split_counts.csv), and [split chart](split_distribution.svg) are derived from the committed manifests in [`splits/`](splits/). The severe imbalance ranges from 4,698 Normal images to 88 Hypertension images.

## Sample images

No source fundus images were supplied outside the excluded multi-gigabyte dataset, so the assignment's eight-class sample-image panel cannot be produced honestly. [`sample_images/README.md`](sample_images/README.md) documents this gap. No substitute or synthetic medical images were added.

These CSVs are the recovered Custom CNN splits. The original ResNet18 split CSVs are missing. Its historical split sizes match, but its test supports differ, so the two test memberships are not identical.
