from feature.feature_generator import FeatureGenerator
from configs.path_config import DATA_PATH_HOME
from feature.breakfaith.breakfaith_count import BreakfaithCount




def get_single():
    fg = FeatureGenerator()
    fg.set_action_list([BreakfaithCount()])
    result = fg.generate()
    result.to_csv(DATA_PATH_HOME + "feature/breakfaith/breakfaith.csv", index=False)


if (__name__ == "__main__"):
    get_single()