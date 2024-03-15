import quantitativeTradingBasics.factors.indicators as indicators
import quantitativeTradingBasics.initialize.database_init as data_init
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')     # 设置matplotlib的GUI后端

#本金倍数
def test_get_pct_change():
    test_data = data_init.get_testdata(['000422'])
    daily_change,pct_change = indicators.get_pct_change(test_data,'Clpr')
    pct_change.plot()
    plt.show()
    print(pct_change)

#收益率
def test_get_yield():
    test_data = data_init.get_testdata(['000422'])
    rate_yield = indicators.get_yield(test_data,'Clpr')
    print(rate_yield)
    rate_yield.plot()
    plt.show()

#测试年化收益率
def test_get_annual_yield():
    test_data = data_init.get_testdata(['000422'])
    annual_yield = indicators.get_annual_yield(test_data,'Clpr')
    print(annual_yield)
    annual_yield.plot()
    plt.show()

#测试最大回撤
def test_get_max_pullback():
    test_data = data_init.get_testdata(['000422'])
    daily_pullback,max_pullback = indicators.get_max_pullback(test_data, 'Clpr')
    print(max_pullback)
    max_pullback.plot()
    plt.show()

#测试夏普比率
def test_get_sharpe_ratio():
    test_data = data_init.get_testdata(['000422'])
    sharpe_ratio = indicators.get_sharpe_ratio(test_data, 'Clpr')
    print(sharpe_ratio)


def test_indicator_main():
    # test_get_pct_change()
    # test_get_yield()
    # test_get_annual_yield()
    # test_get_max_pullback()
    test_get_sharpe_ratio()

test_indicator_main()