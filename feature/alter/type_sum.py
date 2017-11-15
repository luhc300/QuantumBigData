from feature.feature import Feature
import pandas as pd
import numpy as np
import re

class TypeSum(Feature):
    def __init__(self):
        Feature.__init__(self)

    def generate(self):
        alter = pd.read_csv(self._data_home + "public/2alter.csv")
        alter = alter.drop(["ALTDATE", "ALTBE", "ALTAF"], axis=1)
        alter_onehot = pd.get_dummies(data=alter, columns=["ALTERNO"])
        alter_group = alter_onehot.groupby(by=["EID"]).sum()
        #print(alter_group)
        return alter_group.reset_index()

if __name__ == "__main__":
    print(TypeSum().generate())
