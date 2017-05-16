import win32com.client

DAISHIN_STOCK = "A003540"

# Create Object
instMarketEye = win32com.client.Dispatch("CpSysDib.MarketEye")

# SetInputValue
instMarketEye.SetInputValue(0, (4, 67, 70, 111))
instMarketEye.SetInputValue(1, DAISHIN_STOCK)

# BlockRequest
instMarketEye.BlockRequest()

# GetData
def get_data():
    print("현재가: ", instMarketEye.GetDataValue(0, 0))
    print("PER: ", instMarketEye.GetDataValue(1, 0))
    print("EPS: ", instMarketEye.GetDataValue(2, 0))
    print("최근분기년월: ", instMarketEye.GetDataValue(3, 0))


if __name__ == '__main__':
    get_data()