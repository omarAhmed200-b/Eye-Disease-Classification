# Model checkpoints — MISSING FROM RECOVERED SESSION

`best_resnet18_reweighted.pth` **was not recovered** from the original Kaggle session. This repo does not contain a trained model. Do not claim the historic metrics can be recreated from this repository without rerunning training and obtaining the same original split and seed.

To generate a new model, run `notebooks/resnet18_full_reconstructed.ipynb` on Kaggle with GPU and the authorized dataset. Download the generated checkpoint **before ending the session**. New splits/weights may differ from the lost run. Attach saved checkpoints to a GitHub Release / external permitted file host, not Git history.
