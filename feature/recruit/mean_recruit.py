from feature.feature import Feature
import pandas as pd
import numpy as np
import re


class MeanRecruit(Feature):
    def __init__(self):
        Feature.__init__(self)

    def generate(self):
        lawrecruit = pd.read_csv(self._data_home + "public/9recruit.csv")
        lawrecruit = lawrecruit.drop(["WZCODE","RECDATE"], axis=1)
        mean = lawrecruit["RECRNUM"].mean()
        lawrecruit = lawrecruit.fillna(mean)
        lawrecruit_group = lawrecruit.groupby(by=["EID"]).mean()
        return lawrecruit_group.reset_index()

if __name__ == "__main__":
    print(MeanRecruit().generate())
