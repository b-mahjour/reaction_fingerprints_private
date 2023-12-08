import numpy as np
from rdkit import Chem
from rdkit.Chem import DataStructs, AllChem, MACCSkeys
import pandas as pd

# basic function to generate RFPS
def getRxnFP(r, fp_type, summed, reagent_classes, multipliers):
    """
    Generate a reaction fingerprint from a reaction object.
    :param r: reaction object
    :param fp_type: "MACCS" or "Morgan"
    :param summed: True or False
    :param reagent_classes: list of reagent classes
    :param multipliers: list of multipliers
    :return: reaction fingerprint
    """
    if fp_type == "MACCS":
        rxnMatrix = np.zeros((5,167))
    else:
        rxnMatrix = np.zeros((5,2048))
    row = 0
    for k,m in zip(reagent_classes,multipliers):
        sm = getattr(r,k)
        if sm == "NONE":
            fp = np.zeros((1,))
        else:
            mol = Chem.MolFromSmiles(sm)
            fp = np.zeros((1,))
            if fp_type == "MACCS":
                DataStructs.ConvertToNumpyArray(MACCSkeys.GenMACCSKeys(mol), fp)
            else:
                DataStructs.ConvertToNumpyArray(AllChem.GetMorganFingerprintAsBitVect(mol, 4), fp)
        fp = fp*m
        rxnMatrix[row,:] = fp
        row = row + 1
    if summed:
        return np.sum(rxnMatrix, axis=0)
    else:
        return rxnMatrix