from feature.feature import Feature
import pandas as pd
import numpy as np
import re


class InvestHomeCount(Feature):
    def __init__(self):
        Feature.__init__(self)

    def generate(self):
        invest = pd.read_csv(self._data_home + "public/4invest.csv")
        invest = invest.drop(["BTEID","BTBL","BTYEAR","BTENDYEAR"], axis=1)
        invest_onehot = pd.get_dummies(invest, columns=["IFHOME"])
        invest_group = invest_onehot.groupby(by=["EID"]).sum()
        return invest_group.reset_index()

if __name__ == "__main__":
    print(InvestHomeCount().generate())
