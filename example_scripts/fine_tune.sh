#!/bin/bash

python -m molbart.fine_tune \  
  datamodule=molbart.data.seq2seq_data.Uspto50DataModule \
  data_path=C:\Users\lenovo\Chemformer-main-MolecularAI\Chemformer-main-MolecularAI\Chemformer-selected\data\molecular_properties_datasets\individual files\individual files\ADAM17.csv \
  model_path=C:\Users\lenovo\Chemformer-main-MolecularAI\Chemformer-main-MolecularAI\Chemformer-selected\models\fined-tuned\uspto_50\last.ckpt \
  vocabulary_path=bart_vocab_downstream.json \
  task=backward_prediction \
  n_epochs=100 \
  learning_rate=0.001 \
  schedule=cycle \
  batch_size=64 \
  acc_batches=4 \
  augmentation_probability=0.5
