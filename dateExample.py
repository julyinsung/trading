import time

now = time.localtime()

# 각 리턴 타입은 int 이다. 따라서 앞자리수에 0은 없다.
print(now)
print("년: "+ str(now.tm_year))
print("월(1~12): "+ str(now.tm_mon))
print("일(1~31): "+ str(now.tm_mday))
print("시(0~23): "+ str(now.tm_hour))
print("분(0~59): "+ str(now.tm_min))
print("초(0~59): "+ str(now.tm_sec))
print("요일(0~6): "+ str(now.tm_wday))
print("일수: "+ str(now.tm_yday))

# 요일 0(월), 1(화), 2(수), 3(목), 4(금), 5(토), 6(일)
print(now.tm_wday)