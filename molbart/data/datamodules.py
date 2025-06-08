""" Module containing the default datamodules"""
import pandas as pd
from typing import Any, Dict, List, Optional, Tuple
from molbart.data.base import ReactionListDataModule
from molbart.data.base import MoleculeListDataModule
from pathlib import Path
from typing import Any, Dict, List, Tuple
import torch
from rdkit import Chem

class SynthesisDataModule(ReactionListDataModule):
    """
    DataModule for forward and backard synthesis prediction.

    The reactions are read from a tab seperated DataFrame .csv file.
    Expects the dataset to contain SMILES in two seperate columns named "reactants" and "products".
    The dataset must also contain a columns named "set" with values of "train", "val" and "test".
    validation column can be named "val", "valid" or "validation".

    Supports both loading data from file, and in-memory prediction.

    All rows that are not test or validation, are assumed to be training samples.
    """

    datamodule_name = "synthesis"

    def __init__(
            self, 
            reactants: Optional[List[str]] = None, 
            products: Optional[List[str]] = None, 
            **kwargs
        ):
        super().__init__(**kwargs)

        self._in_memory = False
        if reactants is not None and products is not None:
            self._in_memory = True
            print("Using in-memory datamodule.")
            self._all_data = {"reactants": reactants, "products": products}

    def __repr__(self):
        return self.datamodule_name

    def _get_sequences(self, batch: List[Dict[str, Any]], train: bool) -> Tuple[List[str], List[str]]:
        reactants = [item["reactants"] for item in batch]
        products = [item["products"] for item in batch]
        if train:
            reactants = self._batch_augmenter(reactants)
            products = self._batch_augmenter(products)
        return reactants, products

    def _load_all_data(self) -> None:

       
        self.num_workers = 0
        
        if self._in_memory:
            return
        
        if self.dataset_path.endswith(".csv"):
            df = pd.read_csv(self.dataset_path, sep="\t").reset_index()
            self._all_data = {
                "reactants": df["reactants"].tolist(),
                "products": df["products"].tolist(),
            }
            self._set_split_indices_from_dataframe(df)
        else:
            super()._load_all_data()


class ZincDataModule(MoleculeListDataModule):
    """
    DataModule for Zinc dataset.

    The molecules are read as SMILES from a number of
    csv files.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num_workers = 0

    def _load_all_data(self) -> None:
        path = Path(self.dataset_path)
        if path.is_dir():
            dfs = [pd.read_csv(filename) for filename in path.iterdir()]
            df = pd.concat(dfs, ignore_index=True, copy=False)
        else:
            df = pd.read_csv(path)
        self._all_data = {"smiles": df["smiles"].tolist()}
        self._set_split_indices_from_dataframe(df)


class Uspto50DataModule(ReactionListDataModule):
    """
    DataModule for the USPTO-50 dataset

    The reactions as well as a type token are read from
    a pickled DataFrame
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._include_type_token = kwargs.get("include_type_token", False)

    def _get_sequences(self, batch: List[Dict[str, Any]], train: bool) -> Tuple[List[str], List[str]]:
        reactants = [Chem.MolToSmiles(item["reactants"]) for item in batch]
        products = [Chem.MolToSmiles(item["products"]) for item in batch]

        if train:
            reactants = self._batch_augmenter(reactants)
            products = self._batch_augmenter(products)

        if self._include_type_token and not self.reverse:
            reactants = [item["type_tokens"] + smi for item, smi in zip(batch, reactants)]
        if self._include_type_token and self.reverse:
            products = [item["type_tokens"] + smi for item, smi in zip(batch, products)]

        return reactants, products

    def _load_all_data(self) -> None:
        df = pd.read_pickle(self.dataset_path).reset_index()
        self._all_data = {
            "reactants": df["reactants_mol"].tolist(),
            "products": df["products_mol"].tolist(),
            "type_tokens": df["reaction_type"].tolist(),
        }
        self._set_split_indices_from_dataframe(df)


#    def train_dataloader(self):
 #           return DataLoader(
  #              self.train_dataset,
     #           batch_size=self.batch_size,
      #          shuffle=True,
       #         num_workers=0,
        #        pin_memory=True,
         #       prefetch_factor=2,  
          #  )

#    def val_dataloader(self):
 #       return DataLoader(
  #          self.val_dataset,
   #         batch_size=self.batch_size,
    #        shuffle=False,
     #       num_workers=0,
      #      pin_memory=True,
       #     prefetch_factor=2, 
        #)