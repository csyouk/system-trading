import pandas_datareader.data as web
from datetime import datetime
import matplotlib.pyplot as plt

start = datetime(2017, 4, 1)
end = datetime(2017, 4, 15)

gs = web.DataReader("078930.KS", "yahoo", start, end)

if __name__ == '__main__':
    print(gs)
    gs.info(verbose=True)

    plt.plot(gs["Adj Close"])
    plt.show()