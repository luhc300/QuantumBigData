from feature.feature_generator import FeatureGenerator
from configs.path_config import DATA_PATH_HOME
from feature.recruit.recruit_count import RecruitCount
from feature.recruit.mean_recruit import MeanRecruit


def get_single():
    fg = FeatureGenerator()
    fg.set_action_list([RecruitCount(), MeanRecruit()])
    result = fg.generate()
    result.to_csv(DATA_PATH_HOME + "feature/recruit/recruit.csv", index=False)


if (__name__ == "__main__"):
    get_single()