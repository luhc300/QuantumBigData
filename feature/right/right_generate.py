from feature.branch.branch_count import BranchCount
from feature.branch.branch_home_count import BranchHomeCount
from feature.feature_generator import FeatureGenerator
from configs.path_config import DATA_PATH_HOME
from feature.right.right_count import RightCount
from feature.right.right_type_count import RightTypeCount


def get_single():
    fg = FeatureGenerator()
    fg.set_action_list([RightCount(), RightTypeCount()])
    result = fg.generate()
    result.to_csv(DATA_PATH_HOME + "feature/right/right.csv", index=False)


if (__name__ == "__main__"):
    get_single()