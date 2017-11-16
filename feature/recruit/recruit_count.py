from feature.feature import Feature
import pandas as pd
import numpy as np
import re


class RecruitCount(Feature):
    def __init__(self):
        Feature.__init__(self)

    def generate(self):
        recruit = pd.read_csv(self._data_home + "public/9recruit.csv")
        recruit = recruit.drop(["RECRNUM","RECDATE"], axis=1)
        recruit_group = recruit.groupby(by=["EID"]).count()
        return recruit_group.reset_index()

if __name__ == "__main__":
    print(RecruitCount().generate())
