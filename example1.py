import win32com.client

class Example:
    def exam(self):
        instCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
        print(instCpCybos.IsConnect)

        instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
        stockNum = instCpStockCode.GetCount()

        print('\n---------------------')
        # 갯수
        print(instCpStockCode.GetCount())

        print('\n---------------------')
        # 0번째 종목명
        print(instCpStockCode.GetData(1, 0))

        print('\n---------------------')
        # 10개 종목명
        for i in range(0, 10):
            print(instCpStockCode.GetData(1,i))

        print('\n---------------------')
        # 전체에서 naver 종목명 찾기
        for i in range(stockNum):
            if instCpStockCode.GetData(1, i) == 'NAVER':
                print(instCpStockCode.GetData(0,i))
                print(instCpStockCode.GetData(1,i))
                print(i)

        print('\n---------------------')
        # 종목명을 알고 있을때 종목 정보 찾기
        naverCode = instCpStockCode.NameToCode('NAVER')
        naverIndex = instCpStockCode.CodeToIndex(naverCode)
        print(naverCode)
        print(naverIndex)

    def examTest(self):
        return True
aa = Example()
aa.exam()