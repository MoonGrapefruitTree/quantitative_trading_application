import quantitativeTradingBasics.data_processing.data_processing as data_processing
import quantitativeTradingBasics.initialize.database_init as data_init
import matplotlib.pyplot as plt
import matplotlib
import quantitativeTradingBasics.factors.factors as factors

matplotlib.use('TkAgg')     # 设置matplotlib的GUI后端


def test_filter_extreme_percent():
    test_data = data_init.get_testdata(['603098'])
    test_series = test_data['Clpr']
    result_series = data_processing.filter_extreme_percent(test_series)
    result_series.plot()
    test_series.plot()
    plt.show()



def test_filter_extreme_mad():
    test_data = data_init.get_testdata(['603098'])
    test_series = test_data['Clpr']
    result_series = data_processing.filter_extreme_mad(test_series)
    result_series.plot()
    test_series.plot()
    plt.show()


def test_filter_extreme_sigma():
    test_data = data_init.get_testdata(['603098'])
    test_series = test_data['Clpr']
    result_series = data_processing.filter_extreme_sigma(test_series,1)
    result_series.plot()
    test_series.plot()
    plt.show()

def test_standardize():
    test_data = data_init.get_testdata(['603098'])
    test_series = test_data['Clpr']
    result_series = data_processing.standardize(test_series)
    plt.scatter(result_series.index,result_series)
    plt.show()

def test_neutralize():
    test_data = data_init.get_testdata(['603098'])
    test_data = factors.PBR(test_data)
    test_data = test_data[['PBR','Fullshr','NAPS']].dropna()
    result_series = data_processing.neutralize(test_data['PBR'],test_data['Fullshr']*test_data['NAPS'])
    print(result_series)




def main():
    # test_filter_extreme_percent()
    # test_filter_extreme_mad()
    # test_filter_extreme_sigma()
    # test_standardize()
    test_neutralize()


main()