import pandas

pandas.set_option("display.max_rows", None)
pandas.set_option("display.max_columns", None)

df = pandas.read_csv("data/attendance.csv", index_col=0)

#각 컬럼별로 결측치의 갯수 출력
print(df.isnull().sum())
print("\n")

#각 컬럼별로 결측치의 비율 출력
print(df.isnull().sum() / len(df))
print("\n")

#결측값이 있는 레코드 지우기
print(df.dropna())
print("\n")

#결측치를 0으로 채우기
print(df.fillna(0))
print("\n")

#특정 칼럼의 결측치를 해당 칼럼의 평균값으로 채우기
print(df["배구"].fillna(df["배구"].mean()))
print("\n")