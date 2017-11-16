from feature.feature import Feature
import pandas as pd
import numpy as np
import re


class RightTypeCount(Feature):
    def __init__(self):
        Feature.__init__(self)

    def generate(self):
        right = pd.read_csv(self._data_home + "public/5right.csv")
        right = right.drop(["TYPECODE", "ASKDATE", "FBDATE"], axis=1)
        right_onehot = pd.get_dummies(right,columns=["RIGHTTYPE"])
        right_group = right_onehot.groupby(by=["EID"]).sum()
        return right_group.reset_index()


if __name__ == "__main__":
    print(RightTypeCount().generate())
