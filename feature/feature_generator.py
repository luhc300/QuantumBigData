
import pandas as pd
import numpy as np
from configs.path_config import DATA_PATH_HOME
from feature.alter.type_sum import TypeSum


class FeatureGenerator:
    def __init__(self):
        self.__action_list = []

    def set_action_list(self, action_list):
        self.__action_list = action_list

    def append_action_list(self, feature_class):
        self.__action_list.append(feature_class)

    def reset_action_list(self):
        self.__action_list = []

    def generate(self, old_path=None):
        result = None
        flag = True
        if old_path is not None:
            result = pd.read_csv(old_path)
            flag = False
        for action in self.__action_list:
            feature = action.generate()
            if flag:
                result = feature
                flag = False
            else:
                result = pd.merge(result,feature, on="EID")
            print(action.get_feature_name() + " finished")
        return result

