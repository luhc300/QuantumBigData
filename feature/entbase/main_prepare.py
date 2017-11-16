from feature.feature import Feature
import pandas as pd
import numpy as np
import re


class MainPrepare(Feature):
    def __init__(self):
        Feature.__init__(self)

    def generate(self):
        main = pd.read_csv(self._data_home + "public/1entbase.csv")
        main = main.fillna(0)
        return main


if __name__ == "__main__":
    print(MainPrepare().generate())
