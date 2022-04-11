import pandas

laptops_dataframe = pandas.read_csv("./laptops.csv")
print(laptops_dataframe)
print("\n")

#위에 몇 줄만 추출
print(laptops_dataframe.head(5))
print(type(laptops_dataframe.head(5)))
print("\n")

#아래 몇 줄만 추출
print(laptops_dataframe.tail(5))
print("\n")

#DataFrame의 shape 파악
print(laptops_dataframe.shape)
print("\n")

#column정보 확인
print(laptops_dataframe.columns)
print("\n")

#DataFrame컬럼명, 데이터타입, null여부 확인
print(laptops_dataframe.info())
print("\n")

#DataFrame의 통계정보 확인
print(laptops_dataframe.describe())
print("\n")

#가격 오름차순 정렬
print(laptops_dataframe.sort_values(by="price"))
print("\n")

#가격 내림차순 정렬
print(laptops_dataframe.sort_values(by="price", ascending=False))
print("\n")

#Series에서 unique한 값들 추출
print(laptops_dataframe["brand"].unique())
print("\n")

#Series에서 각 값이 몇 번씩 등장하는지 추출
print(laptops_dataframe["brand"].value_counts())
print("\n")

#Series의 통계정보 확인
print(laptops_dataframe["brand"].describe())