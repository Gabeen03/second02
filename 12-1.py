import pandas as pd
folder = "data/"
target = folder + "fktemp.csv"
df = pd.read_csv(target)

# rank 매기기

df["average"] = df.postcode.rank(method="average")
print(df[["postcode", "aver"]])

df["dense"] = df.postcode.rank(method="dense")
print(df[["postcode", "dense"]])

df["first"] = df.postcode.rank(method="first")
print(df[["postcode", "first"]])


df["min"] = df.postcode.rank(method="min")
print(df[["postcode", "min"]])

df["max"] = df.postcode.rank(meethod="max", ascending=False)
df["max"] = df.postcode.rank(method="max")
print(df[["postcode", "max"]])

print(df[["postcode", "max", "min", "first", "dense", "average"]])

# 컬럼-로우 변경
print(df.transpose())

# 누적계산
print(df["postcode"].expanding().sum())

# 정렬 찾기
""" 
print(df.postcode.idxmax(axis=0)) = 가장 작은 수
print(df.postcode.idxmin(axis=0)) = 가장 큰 수
 """

# empty 추가
print(df.empty())
print(df.company.empty)

# 검색
print(df.isin(48742))
print(df.isin(["문상훈"]))

# print(df.isin([48742, 12834]))

# print(df.isin(48742, 12834, "문상훈"))

# 기간 계산

""" period = pd.period_range(start="2023-11-10 00:00:00", end="2023-11-10 02:30:00", freq="30T")
dt = {"col1":[1,2,3,4,5,6],"col2":period}
idx = ["row1","row2","row3","row4","row5","row6"]
pf = pd.DataFrame(data=dt, index=idx)
print(pf) """

# 인덱스 시간 - 간격 생성

# i = pd.date_range("2023-11-10", periods=10, freq="1H")

i = pd.date_range("2023-11-10", periods=10, freq="3H")
df = pd.DataFrame({"col1":[1,2,3,4,5,6,7,8,9,10]}, index=i)
print(df)

print("\n---------------------------- \n")
# 특정시간 인덱스 찾기
print(df.at_time("09:00"))
print(df.at_time("03:00"))

# 범위 찾기
print(df.between_time(start_time="12:00", end_time="00:00"))

# X일 간격 생성 - 기간별 찾기

i = pd.date_range("2023-11-10", periods=10, freq="3D")
# i = pd.date_range("2023-11-10", periods=10, freq="5D")
df = pd.DataFrame({'col1':[1,2,3,4,5,6,7,8,9,10]}, index=i)
print(df)

print(df.first("5D"))

# print(df.first("7D"))

# 코스피지수 확인
# pip install FinanceDataReader
import FinanceDataReader as fdr

ksp = fdr.DataReader("KS11", "2001" )
print(ksp)
print("\n---------------------------- \n")

# 최고가

res = ksp["High"].max()
print(res)

res = ksp["High"].idxmax()
print(res)

# 최저가
res = ksp["Low"].min()
print(res)

res = ksp["Low"].idxmin()
print(res)

# 최고가 값 찾기
res= ksp["Volume"].nlargest(n=5)
# res= ksp["Volume"].nlargest(n=10)
print(res)

# 최하위 값 찾기
res = ksp["Volume"].nsmallest(n=5)
# res = ksp["Close"].nsmallest(n=5)
# res = ksp["Close"].nlargest(n=5)
print(res)

# kospi 3000 달성 최초일 찾기

cond = ksp["Close"] >= 3000
# cond = ksp["Close"] >= 2000
res = ksp[cond].index[0]
print(res)

# 위(shift) 값 참조, 처리

ksp["up"] = ksp["Volume"] > ksp["Volume"].shift()
print(ksp)

res = ksp["up"] != ksp["up"].shift().cumsum()
print(res)

ksp["grp"] = (ksp["up"] != ksp["up"].shift()).cumsum()
print(ksp)

# 연속 증가값 확인
ksp["grp"].groupby(ksp["grp"].values).cumcount() + 1
print(ksp)

print(ksp["up_cnt"].max())

# 변환

import pandas as pd

target = "./data/apt.csv"

df = pd.read_csv(target, encoding="CP949")

df.to_csv("./data/apt.csv", encoding="utf8")

print(df.head())




df = pd.read_csv("./data/conv_apt.csv", index_col=0)
print(df.head())



# 컬럼명 바꾸기

df = df.rename(columns={"분양가격(제곱미터)":"분양가"})
# print(df)
# print(df.dtypes)

# 컬럼 타입변경

df["분양가"] = df["분양가"].convert_dtypes()
# print(df.dtypes)

# array 변환 

arr =df.to_numpy()
# print(arr)
# print(arr[2])
# print(len(arr))

# 요약정보
print(df.describe())

# 축변환하기
print(df.transpose())
print("\n------------------------\n")
print(df.T.head())

