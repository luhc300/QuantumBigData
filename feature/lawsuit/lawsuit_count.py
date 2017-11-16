from feature.feature import Feature
import pandas as pd
import numpy as np
import re


class LawsuitCount(Feature):
    def __init__(self):
        Feature.__init__(self)

    def generate(self):
        lawsuit = pd.read_csv(self._data_home + "public/7lawsuit.csv")
        lawsuit = lawsuit.drop(["LAWDATE","LAWAMOUNT"], axis=1)
        lawsuit_group = lawsuit.groupby(by=["EID"]).count()
        return lawsuit_group.reset_index()

if __name__ == "__main__":
    print(LawsuitCount().generate())
