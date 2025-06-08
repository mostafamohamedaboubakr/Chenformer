import pickle
import pandas as pd

# Path to your full input pickle file
#input_path = r"C:\Users\lenovo\Chemformer-main-MolecularAI\Chemformer-main-MolecularAI\Chemformer-selected\data\seq-to-seq_datasets\uspto_50.pickle"
input_path = "/mnt/c/Users/lenovo/Chemformer-main-MolecularAI/Chemformer-main-MolecularAI/Chemformer-selected/data/seq-to-seq_datasets/uspto_50.pickle"

output_path = "/mnt/c/Users/lenovo/Chemformer-main-MolecularAI/Chemformer-main-MolecularAI/Chemformer-selected/data/seq-to-seq_datasets/uspto_50_1000.pickle"


# Load the full DataFrame
df = pd.read_pickle(input_path)
print(f" Loaded {len(df)} rows")

# Keep just the first 10 rows
df_small = df.head(1000)

# Save the smaller DataFrame
df_small.to_pickle(output_path)

print(f" Saved 10-sample DataFrame to: {output_path}")
