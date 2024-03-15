import quantitativeTradingBasics.factors.factors as factors
import quantitativeTradingBasics.initialize.database_init as data_init
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')     # 设置matplotlib的GUI后端


##  mean7 and mean30
def test_mean():
    test_data = data_init.get_testdata(['603098'])
    test_data_mean7 = factors.mean7(test_data,'Clpr')
    test_data_mean30 = factors.mean_all(test_data,'Clpr', 30)
    test_data['mean7'] = test_data_mean7
    test_data['mean30'] = test_data_mean30
    test_data[['Clpr','mean7','mean30']].plot()
    plt.show()

def test_PBR():
    test_data = data_init.get_testdata(['603098'])
    test_data = factors.PBR(test_data)
    test_data['PBR'].plot()
    plt.show()

def test_factor_main():
    # test_mean()
    test_PBR()


test_factor_main()