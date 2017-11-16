from feature.alter.type_sum import TypeSum
from feature.feature_generator import FeatureGenerator
from configs.path_config import DATA_PATH_HOME

def get_single():
    fg = FeatureGenerator()
    fg.set_action_list([TypeSum()])
    result = fg.generate()
    result.to_csv(DATA_PATH_HOME + "feature/alter/alter.csv", index=False)


if (__name__ == "__main__"):
    get_single()