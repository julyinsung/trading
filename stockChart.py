import win32com.client

# Create object
instStockChart = win32com.client.Dispatch("CpSysDib.StockChart")

# SetInputValue

# 0은 종목 코드를 의미하고, 'A003540'은 조회하려는 종목의 코드값
instStockChart.SetInputValue(0, "A003540")

# 기간으로 요청 '1'을 입력하고, 개수로 요청'2'를 입력합니다.
# 다만 파이썬의 문자열을 그대로 입력하는 것이 아니라
# ord라는 함수를 통해 문자열 값을 아스키코드(ASCII code)로 변환
instStockChart.SetInputValue(1, ord('2'))

# 세 번째로 입력한 데이터는 요청 개수입니다.
# SetInputValue(4, 10)에서 4가 요청 개수라는 타입을 의미하고
# 10이 실제로 요청할 데이터의 개수를 의미합니다.
# 10은 최근 거래일로부터 10일치의 데이터를 의미합니다.
instStockChart.SetInputValue(4, 10)

# 네 번째로 입력한 데이터는 요청할 데이터 종류입니다.
# CYBOS Plus 도움말에 있는 StockChart 부분을 참조하면
# 종가에 해당하는 값이 5임을 알 수 있습니다.
instStockChart.SetInputValue(5, (0, 2, 3, 4, 5, 8))

# 다섯 번째로 입력한 데이터는 차트의 종류로
# 일 단위의 데이터를 얻기 위해 ord('D')를 입력해주었습니다.
instStockChart.SetInputValue(6, ord('D'))

# 여섯 번째로 입력한 데이터는 수정 주가의 반영 여부에 대한 것으로
# 수정 주가를 의미하는 ord('1')을 입력했습니다.
instStockChart.SetInputValue(9, ord('1'))

# BlockRequest
instStockChart.BlockRequest()

# GetHeaderValue
numData = instStockChart.GetHeaderValue(3)
numFiled = instStockChart.GetHeaderValue(1)

# GetDataValue
for i in range(numData):
    for j in range(numFiled):
        print(instStockChart.GetDataValue(j, i), end=" ")
    print("")