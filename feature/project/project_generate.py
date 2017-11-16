from feature.feature_generator import FeatureGenerator
from configs.path_config import DATA_PATH_HOME
from feature.project.project_count import ProjectCount
from feature.project.project_home_count import ProjectHomeCount



def get_single():
    fg = FeatureGenerator()
    fg.set_action_list([ProjectCount(), ProjectHomeCount()])
    result = fg.generate()
    result.to_csv(DATA_PATH_HOME + "feature/project/project.csv", index=False)


if (__name__ == "__main__"):
    get_single()