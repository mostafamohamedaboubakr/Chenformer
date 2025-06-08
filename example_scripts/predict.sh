#!/bin/bash

python -m molbart.predict \
  data_path=/mnt/c/Users/lenovo/Chemformer-main-MolecularAI/Chemformer-main-MolecularAI/Chemformer-selected/data/seq-to-seq_datasets/uspto_50_10.pickle 
  vocabulary_path=bart_vocab_downstream.json \
  model_path=/mnt/c/Users/lenovo/Chemformer-main-MolecularAI/Chemformer-main-MolecularAI/Chemformer-selected/models/fined-tuned/uspto_50/last.ckpt 
  task=forward_prediction \
  output_sampled_smiles=Chemformer-main-MolecularAI/Chemformer-main-MolecularAI/experiment_1/fine_tune_out/predicted_products.csv 
  batch_size=64 \
  n_beams=10
  datamodule=Uspto50DataModule