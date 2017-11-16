from feature.feature import Feature
import pandas as pd
import numpy as np
import re


class BreakfaithCount(Feature):
    def __init__(self):
        Feature.__init__(self)

    def generate(self):
        breakfaith = pd.read_csv(self._data_home + "public/8breakfaith.csv")
        breakfaith = breakfaith.drop(["FBDATE","SXENDDATE"], axis=1)
        breakfaith_group = breakfaith.groupby(by=["EID"]).count()
        return breakfaith_group.reset_index()

if __name__ == "__main__":
    print(BreakfaithCount().generate())
