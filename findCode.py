import win32com.client

instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")

# 전체 종목 갯수
print(instCpStockCode.GetCount())
print('\n')

# 첫 번째 인자의 값이 0이면 종목 코드를, 1이면 종목명을, 2이면 FullCode를 리턴
# 두 번째 인자는 n 번째 주식 종목을 말함.
print(instCpStockCode.GetData(1, 0))
print('\n')

print(instCpStockCode.GetData(0, 0))
print('\n')

# 0 부터 10개의 종목명 출력
for i in range(0, 10):
    print(instCpStockCode.GetData(1,i))

print('\n')

# NAVER 종목코드 종목명 찾기
stockNum = instCpStockCode.GetCount()

for i in range(stockNum):
    if instCpStockCode.GetData(1, i) == 'NAVER':
        print(instCpStockCode.GetData(0,i))
        print(instCpStockCode.GetData(1,i))
        print(i)

print('\n')

#  NAVER 종목코드 종목명 찾기 다른 방법
naverCode = instCpStockCode.NameToCode('NAVER')
naverIndex = instCpStockCode.CodeToIndex(naverCode)
print(naverCode)
print(naverIndex)