import quantitativeTradingBasics.strategies.strategies as strategies
import quantitativeTradingBasics.initialize.database_init as data_init
import quantitativeTradingBasics.factors.indicators as indicators
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')     # 设置matplotlib的GUI后端

def test_gold_and_dead_fork():
    test_data = data_init.get_testdata(['603098'])
    data, gd_pct_change = strategies.gold_and_dead_fork(test_data, 'Clpr', 5, 30,True)
    daily_change,pct_change = indicators.get_pct_change(test_data, 'Clpr')
    pct_change['gd_pct'] = gd_pct_change
    pct_change['excess_earnings'] = pct_change['gd_pct']-pct_change['pct_change']
    print(data,gd_pct_change,pct_change)
    gd_pct_change.plot()
    plt.show()


def test_gold_and_dead_fork_adaptive_parameter():
    test_data = data_init.get_testdata(['603098'])
    result ,gdap_gd_pct_change = strategies.gold_and_dead_fork_adaptive_parameter(test_data, 'Clpr',[5,10,30,60,90,180],[5,10,30,60,90,180])

    print(result)
    print(gdap_gd_pct_change)
    gdap_gd_pct_change.plot()
    plt.show()

def test_stratrgies_mian():
    test_gold_and_dead_fork()

    # test_gold_and_dead_fork_adaptive_parameter()

test_stratrgies_mian()