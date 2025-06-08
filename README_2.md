# Updated Chemformer Repository

This is a README file for the Chemfromer repo (updated with all new versions of packages and dependencies till june 2025), it contains a quick guid to test the the fine-tuning and prediction tasks. It includes a guide for Chemformer users working in resource-limited or single-GPU environments.

## Setup Instructions

### Linux / Ubuntu

1. Clone the repository:

   ```bash
   git clone https://github.com/[your-fork-or-source]/Chemformer.git
   cd Chemformer
   ```

2. Create and activate a conda environment:

   ```bash
   conda create -n chemformer python=3.10
   conda activate chemformer
   ```

3. Install dependencies manually:

   ```bash
   pip install torch pytorch-lightning rdkit pandas hydra-core
   ```

### Windows (via WSL Recommended)

1. Enable [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install).
2. Open Ubuntu via WSL and follow the Linux setup steps above.
3. Ensure GPU access with `nvidia-smi` and install CUDA-enabled PyTorch if needed:

   ```bash
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
   ```

---

## Directory Structure

```
Chemformer/
├── molbart/
│   ├── fine_tune.py
│   ├── predict.py
│   ├── inference_score.py
│   ├── build_tokenizer.py
│   ├── retrosynthesis/
│   │   └── round_trip_inference.py
├── Chemformer-selected/
│   ├── data
│   ├── model
├── example_scripts/
├── limit_input.py
├── experiment_1/
│   ├── fine_tune2.yaml
│   └── predict.yaml
```

---

##  Running the Scripts

### 1. Fine-Tuning a Model

```bash
python -m molbart.fine_tune --config-path=experiment_1 --config-name=fine_tune2.yaml
```

> Make sure `fine_tune.yaml` is configured with the right paths and checkpoint.

### 2. Predicting Molecules

```bash
python -m molbart.predict --config-path=experiment_1 --config-name=predict.yaml
```
---

## Using `limit_input.py` to Slice Dataset

### Purpose:

Create a smaller subset from a large `.pickle` dataset (e.g., `uspto_50.pickle`), you can find the dataset and model chackpoints [here](https://az.box.com/s/7eci3nd9vy0xplqniitpk02rbg9q2zcq).

### Example:

```bash
python limit_input.py
```

### Required Edits:

Open `limit_input.py` and configure these lines:

```python
input_path = "path/to/original_dataset.pickle"
output_path = "path/to/limited_dataset.pickle"
N = 10  # number of samples to keep
```

> Then run the script to create a smaller dataset for testing.

---


---

## References

* [Chemformer Paper (Irwin et al., 2022)](https://arxiv.org/abs/2106.09430)
* [USPTO-50 Dataset](https://figshare.com/articles/dataset/USPTO_reaction_dataset/5104873)
* [RDKit Documentation](https://www.rdkit.org/docs/index.html)

---

