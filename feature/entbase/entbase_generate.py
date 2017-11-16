from feature.feature_generator import FeatureGenerator
from configs.path_config import DATA_PATH_HOME
from feature.entbase.main_prepare import MainPrepare


def get_single():
    fg = FeatureGenerator()
    fg.set_action_list([MainPrepare()])
    result = fg.generate()
    result.to_csv(DATA_PATH_HOME + "feature/entbase/entbase.csv", index=False)


if (__name__ == "__main__"):
    get_single()