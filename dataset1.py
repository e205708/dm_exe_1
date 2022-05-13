import math
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
#フォント設定
import matplotlib.font_manager as font_manager
font_path = '/Library/Fonts/Arial Unicode.ttf'
font_prop = font_manager.FontProperties(fname = font_path)
matplotlib.rcParams['font.family'] = font_prop.get_name()

def true_function(x):
    '''
    >>> true_function(0)
    0.0
    '''
    y = math.sin(math.pi*x*0.8)*10
    return y



if __name__ == '__main__':
    import doctest
    doctest.testmod()

    #-1から1まで100等分
    x = np.linspace(-1, 1, 100,endpoint=True)

    #true_functionをユニバーサル関数に変換
    u_true_function = np.frompyfunc(true_function,1,1)
    y = u_true_function(x)

    #グラフの設定
    plt.title('ex1.1')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x,y)    

    #グラフの出力
    plt.savefig("ex1.1.png")
    plt.show()



