import pandas

iphone_dataframe = pandas.read_csv("data/iphone.csv", index_col=0)
print(iphone_dataframe)
print("\n")

#하나의 값 수정
iphone_dataframe.loc["iPhone 7", "메모리"] = "3GB"
print(iphone_dataframe)
print("\n")

#한 row의 모든 값 수정
iphone_dataframe.loc["iPhone 7 Plus"] = ["2016-09-20", "5.6", "4GB", "iOS 10.1", "No"]
print(iphone_dataframe)
print("\n")

#한 column의 모든 값 수정
iphone_dataframe["디스플레이"] = ["4.6", "5.5", "4.6", "5.4", "5.7", "5.7", "6.4"]
print(iphone_dataframe)
print("\n")

#한 column의 모든 값 똑같이 수정
iphone_dataframe["Face ID"] = "No"
print(iphone_dataframe)
print("\n")

#여러 column 한꺼번에 수정
iphone_dataframe[["디스플레이", "Face ID"]] = "A"
print(iphone_dataframe)
print("\n")

#여러 row 한꺼번에 수정
iphone_dataframe.loc[["iPhone 7", "iPhone 8"]] = "B"
print(iphone_dataframe)
print("\n")

#조건으로 row선택 후 수정
iphone_dataframe = pandas.read_csv("data/iphone.csv", index_col=0)
condition = iphone_dataframe["디스플레이"] > 5
iphone_dataframe.loc[condition] = "C"
print(iphone_dataframe)
print("\n")

#위치로 값 변경
iphone_dataframe.iloc[[1, 3], [2, 4]] = "D"
print(iphone_dataframe)
print("\n")