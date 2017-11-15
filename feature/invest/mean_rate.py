from feature.feature import Feature
import pandas as pd
import numpy as np
import re


class MeanRate(Feature):
    def __init__(self):
        Feature.__init__(self)

    def generate(self):
        invest = pd.read_csv(self._data_home + "public/4invest.csv")
        invest = invest.drop(["BTEID","IFHOME","BTYEAR","BTENDYEAR"], axis=1)
        invest_group = invest.groupby(by=["EID"]).mean()
        return invest_group.reset_index()

if __name__ == "__main__":
    print(MeanRate().generate())
