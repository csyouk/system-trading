import win32com.client
instCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")

instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")

CONNECTED = 1

def get_default():
    print(instCpCybos.IsConnect == CONNECTED)
    # print(dir(instCpCybos))

    print("Number of Stocks in Market : {}".format(instCpStockCode.GetCount()))
    print(instCpStockCode.GetData(0, 0))

    for stock in range(0, instCpStockCode.GetCount()):
        name = instCpStockCode.GetData(1, stock)
        print(name)
        if name == "삼성전자":
            print("="*30)
            print(instCpStockCode.GetData(2, stock))
            print("=" * 30)

if __name__ == "__main__":
    get_default()