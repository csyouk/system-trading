import win32com.client
instStockChart = win32com.client.Dispatch("CpSysDib.StockChart")

DAISHIN_STOCK = "A003540"

def get_past_data():
    instStockChart.SetInputValue(0, DAISHIN_STOCK)
    instStockChart.SetInputValue(1, ord('2'))
    instStockChart.SetInputValue(4, 10)
    instStockChart.SetInputValue(5, 5)
    instStockChart.SetInputValue(6, ord('D'))
    instStockChart.SetInputValue(9, ord('1'))

    instStockChart.BlockRequest()

    numData = instStockChart.GetHeaderValue(3)
    for i in range(numData):
        print(instStockChart.GetDataValue(0, i))


if __name__ == '__main__':
    get_past_data()
