import win32com.client

instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
codeList = instCpCodeMgr.GetStockListByMarket(1)

kospi = {}
for code in codeList:
    name = instCpCodeMgr.CodeToName(code)
    kospi[code] = name


def dump_to_csv():
    f = open('c:\\Users\\YOUK\\PycharmProjects\\system-trading\\ch10\\kospi.csv', 'w')
    for key, value in kospi.items():
        f.write("%s,%s\n" % (key, value))
    f.close()


if __name__ == '__main__':
    dump_to_csv()
