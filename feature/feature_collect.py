import pandas as pd
import numpy as np
from configs.path_config import DATA_PATH_HOME

def get_all_feature(feature_list):
    result = None
    flag = False
    for feature in feature_list:
        data = pd.read_csv(DATA_PATH_HOME + "feature/" + feature + "/" + feature + ".csv")
        if not flag:
            flag = True
            result = data
        else:
            result = pd.merge(result, data, on="EID",how="left")
    result = result.fillna(0)
    return result

def get_train(data):
    train_set = pd.read_csv(DATA_PATH_HOME + "public/train.csv")
    result = pd.merge(train_set, data, on="EID")
    return result

def get_test(data):
    test_set = pd.read_csv(DATA_PATH_HOME + "public/evaluation_public.csv")
    result = pd.merge(test_set, data, on="EID")
    return result

if __name__ == "__main__":
    feature_list = ["entbase", "alter", "branch", "invest", "right"]
    feature_total = get_all_feature(feature_list)
    feature_total.to_csv(DATA_PATH_HOME + "feature/total.csv", index=False)
    train = get_train(feature_total)
    test = get_test(feature_total)
    train.to_csv(DATA_PATH_HOME + "feature/train.csv", index=False)
    test.to_csv(DATA_PATH_HOME + "feature/test.csv", index=False)