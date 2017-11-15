from feature.feature import Feature
import pandas as pd
import numpy as np
import re


class BranchHomeCount(Feature):
    def __init__(self):
        Feature.__init__(self)

    def generate(self):
        branch = pd.read_csv(self._data_home + "public/3branch.csv")
        branch = branch.drop(["TYPECODE", "B_REYEAR", "B_ENDYEAR"], axis=1)
        branch_onehot = pd.get_dummies(branch, columns=["IFHOME"])
        branch_group = branch_onehot.groupby(by=["EID"]).sum()
        return branch_group.reset_index()

if __name__ == "__main__":
    print(BranchHomeCount().generate())
