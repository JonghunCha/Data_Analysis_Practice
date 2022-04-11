import pandas

iphone_dataframe = pandas.read_csv("./iphone.csv", index_col=0)
print(iphone_dataframe)
print("\n")

#row한 줄 추가하기
iphone_dataframe.loc["iPhone XR"] = ["2018-10-26", 6.1, "3GB", "iOS 12.0.1", "Yes"]
print(iphone_dataframe)
print("\n")

#column한 줄 추가하기
iphone_dataframe["제조사"] = "Apple"
print(iphone_dataframe)
print("\n")

#row한 줄 삭제하기
#axis="index"는 row를 삭제함을, axis="columns"는 column을 삭제함을 의미
#inplace가 False면 새로운 DataFrame을 생성, True면 기존 DataFrame에 덮어씀을 의미
iphone_dataframe.drop("iPhone XR", axis="index", inplace=True)
print(iphone_dataframe)
print("\n")

#column한 줄 삭제하기
iphone_dataframe.drop("제조사", axis="columns", inplace=True)
print(iphone_dataframe)
print("\n")

#여러 row 한 번에 삭제하기
iphone_dataframe.drop(["iPhone 7", "iPhone 7 Plus"], axis="index", inplace=True)
print(iphone_dataframe)
print("\n")

#여러 column 한 번에 삭제하기
iphone_dataframe.drop(["Face ID", "출시 버전"], axis="columns", inplace=True)
print(iphone_dataframe)
print("\n")