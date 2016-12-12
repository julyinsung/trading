import win32com.client

instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
codeList = instCpCodeMgr.GetStockListByMarket(1)

for i, code in enumerate(codeList):
    #  1번이 주권, 10번이 ETF, 17번이 ETN
    secondCode = instCpCodeMgr.GetStockSectionKind(code)
    name = instCpCodeMgr.CodeToName(code)
    if secondCode == 1:
        print(i, code, secondCode, name)