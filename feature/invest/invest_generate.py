from feature.feature_generator import FeatureGenerator
from configs.path_config import DATA_PATH_HOME
from feature.invest.invest_count import InvestCount
from feature.invest.invest_home_count import InvestHomeCount
from feature.invest.mean_rate import MeanRate


def get_single():
    fg = FeatureGenerator()
    fg.set_action_list([InvestCount(), InvestHomeCount(), MeanRate()])
    result = fg.generate()
    result.to_csv(DATA_PATH_HOME + "feature/invest/invest.csv", index=False)


if (__name__ == "__main__"):
    get_single()