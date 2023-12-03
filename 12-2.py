import pandas as pd

target = './data/apt.csv'
df = pd.read_csv(target, encoding = "CP949")

df.to_csv("./data/conv_apt.csv", encoding="utf8")

print(df.head())

df = pd.read_csv("./data/conv_apt.csv", index_col=0)
print(df.head())

df = pd.read_csv("./data/conv_apt.csv", index_col=0)
print(df.head()) 

# 컬럼명 바꾸기 
""" df = pd.read_csv("./data/conv_apt.csv", index_col=0)
df= df.rename(columns={"분양가격(제곱미터)": "분양가"})
res = df.sort_values("지역명")
df.reset index(inplace=True)
ascending-False
print (res.head ())
res = df.sort_values(by="연도")[10:28]
print(res)
res = df[["지역명", "연도", "분양가"]][:]
print (res) """

# res = df.sort_values(by="지역명")[:5]
# print(res)

# res = df.sort(values(by="지역명"))
# res = df.sort(values("지역명"))
# res = df.sort_values("지역명", ascending=True)
res = df.sort_values("지역명", ascending=False)
# print(res.head(10))
print(res.head())

res = df.sort_values(by="연도")
# res = df.sort_values(by="분양가")
res = df.sort_values(by="연도")[10:20]
print(res)
# res(head)와 동일한 값으로 출력됨

# 컬럼이름 출력

res = df["지역명"[:5]]
res = df[["지역명", "연도"]]
res = df[["지역명", "연도", "분양가"]]
res = df[["지역명", "연도"]][:5]
print(res)

print("\n-------------------------\n")
res = df.loc[:, ["지역명", "연도"]][:5]
# res = df.loc[:][:5]
# res = df.loc[:][:]
res = df.iloc[1]
print(res)

res = df.loc[:6, ["지역명", "연도"]]
# res = df.loc[:6, ["지역명", "연도"]][:3] # 3까지만 출력하라
# res = df.loc[:6, ["지역명", "연도"]][:7]

# 필터 출력

df.loc[df["지역명"]=="강원"]
# df.loc[df["연도"] > 2020]
df.loc[df["지역명"]=="서울",["지역명", "연도", "분양가"]]
# df.loc[df["지역명"]=="서울",["지역명", "연도", "분양가"]][:10]
# df.loc[df["지역명"]=="서울",["지역명", "연도", "분양가"]][-10:]
print(res)

# 인덱스 지정 선택

dfo = df.copy()
print(dfo)

print("\n------------------------------\n")
res= df.iloc[2]
res(df.iloc[2][4])
print(res)

# 인덱스 필터
res = df[df.index > 3560]
print(res)

# 필터

res = df[df.연도 == 2023]
res = df[df.월 ==3]
print(res)

# 비트연산 필터
# df[(df.연도 == 2023) & (df.지역명 == "서울")]
df[(df.연도 == 2023) & (df.지역명 == "서울") & (df.월 == 6)]
print(res)

# 컬럼 추가

columns=list(df.columns)
print(columns + "컬럼")

# df1 = df.reindex(index=df.index[:7], columns=list(df.columns) + ["extra"])
df1 = df.reindex(columns=list(df.columns), columns=list(df.columns) + ["extra"])
print(df)
print("\n------------------------------\n")
print(df1)

print("\n------------------------------\n")
df1.loc[:6, "extra"] = "0"
df1.loc[:4, "extra"] = False
print(df1)

# 복사
df2 = df1.copy()

# NaN 행 제거
# res = df2.dropna(how="any")
res = df2.fillna(value="1234")
print(res)
res = df2.dropna(how="any", inplace=True) # inplace=TRue 해야 실행 가능함
print(res)

print("\n------------------------------\n")
print(df2)


res = pd.isna(df1)
# res = pd.isna(df)
# res = pd.isna(df0)
# res = pd.isna(df2)
print(res)

# 데이터 종류별 출력
res = df["연도"].value_counts()
# res = df["지역명"].value_counts()
# res = df["월"].value_counts()
# res = df.월.value_counts() # dataframe 이 객체이기 때문에 가능함
print(res)

# 그룹핑
res = df.groupby(["지역명", "연도", "월"]).sum()
# res = df.groupby(["지역명", "연도", "월"]).all()
print(res)


print("\n------------------------------\n")
print(df.mean())

res = df.groupby(["지역명", "연도", "월", "분양가"])["분양가"].agg("sum")
print(res)

# 타이타닉

tr = pd.read_csv("C:\\Users\\Catholic\\python\\happy\\data\\train.csv", index_col=0, encoding='cp949')
res = tr.isnull().sum()
print(res)
print("\n----------------------\n")
res = pd.crosstab(tr["Embarked"], tr["Survived"])
print(res)
print("\n----------------------\n")

# 컬럼 매핑
res = res.columns.map({0:"Dead", 1:"Alive"})
print(res)
print("\n----------------------\n")