import win32com.client

DAISHIN_STOCK = "A003540"

# Create object
instStockChart = win32com.client.Dispatch("CpSysDib.StockChart")

# SetInputValue
instStockChart.SetInputValue(0, DAISHIN_STOCK)
instStockChart.SetInputValue(1, ord('2'))
instStockChart.SetInputValue(4, 60)
instStockChart.SetInputValue(5, 8)
instStockChart.SetInputValue(6, ord('D'))
instStockChart.SetInputValue(9, ord('1'))

# BlockRequest
instStockChart.BlockRequest()

# GetData
def get_data():
    volumes = []
    numData = instStockChart.GetHeaderValue(3)
    for i in range(numData):
        volume = instStockChart.GetDataValue(0, i)
        volumes.append(volume)
    print(volumes)

    # Calculate average volume
    averageVolume = (sum(volumes) - volumes[0]) / (len(volumes) - 1)

    if (volumes[0] > averageVolume * 10):
        print("대박주")
    else:
        print("일반주", volumes[0] / averageVolume)

if __name__ == '__main__':
    get_data()