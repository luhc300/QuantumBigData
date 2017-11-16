from feature.feature import Feature
import pandas as pd
import numpy as np
import re


class ProjectHomeCount(Feature):
    def __init__(self):
        Feature.__init__(self)

    def generate(self):
        project = pd.read_csv(self._data_home + "public/6project.csv")
        project = project.drop(["TYPECODE","DJDATE"], axis=1)
        project_onehot = pd.get_dummies(project, columns=["IFHOME"])
        project_group = project_onehot.groupby(by=["EID"]).sum()
        return project_group.reset_index()

if __name__ == "__main__":
    print(ProjectHomeCount().generate())
