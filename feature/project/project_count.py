from feature.feature import Feature
import pandas as pd
import numpy as np
import re


class ProjectCount(Feature):
    def __init__(self):
        Feature.__init__(self)

    def generate(self):
        project = pd.read_csv(self._data_home + "public/6project.csv")
        project = project.drop(["DJDATE","IFHOME"], axis=1)
        project_group = project.groupby(by=["EID"]).count()
        return project_group.reset_index()

if __name__ == "__main__":
    print(ProjectCount().generate())
