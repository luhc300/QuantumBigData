from feature.feature_generator import FeatureGenerator
from configs.path_config import DATA_PATH_HOME
from feature.invest.invest_count import InvestCount
from feature.invest.invest_home_count import InvestHomeCount
from feature.invest.mean_rate import MeanRate
from feature.lawsuit.lawsuit_count import LawsuitCount
from feature.lawsuit.mean_suit import MeanSuit


def get_single():
    fg = FeatureGenerator()
    fg.set_action_list([LawsuitCount(), MeanSuit()])
    result = fg.generate()
    result.to_csv(DATA_PATH_HOME + "feature/lawsuit/lawsuit.csv", index=False)


if (__name__ == "__main__"):
    get_single()