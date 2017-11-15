from feature.feature import Feature
import pandas as pd
import numpy as np
import re


class BranchCount(Feature):
    def __init__(self):
        Feature.__init__(self)

    def generate(self):
        branch = pd.read_csv(self._data_home + "public/3branch.csv")
        branch = branch.drop(["IFHOME", "B_REYEAR", "B_ENDYEAR"], axis=1)
        branch_group = branch.groupby(by=["EID"]).count()
        return branch_group.reset_index()

if __name__ == "__main__":
    print(BranchCount().generate())
