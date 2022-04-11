import pandas

iphone_dataframe = pandas.read_csv("./iphone.csv", index_col=0)
print(iphone_dataframe)
print("\n")

#row명과 col이름을 통해 원하는 값 추출하기
print(iphone_dataframe.loc["iPhone 8", "메모리"])
print(iphone_dataframe.loc["iPhone X", "출시 버전"])
print("\n")

#row 한 줄 전체를 추출하기
print(iphone_dataframe.loc["iPhone XS", :])
print("\n")
print(iphone_dataframe.loc["iPhone XS"])
print("\n")

#column 한 줄 전체를 추출하기
print(iphone_dataframe.loc[:, "디스플레이"])
print("\n")
print(iphone_dataframe["디스플레이"])
print("\n")

#row 여러 줄 전체를 추출하기
print(iphone_dataframe.loc[["iPhone 7", "iPhone 7 Plus"], :])
print("\n")
print(iphone_dataframe.loc[["iPhone 7", "iPhone 7 Plus"]])
print("\n")
print(iphone_dataframe.loc["iPhone 7" : "iPhone X"])
print("\n")

#column 여러 줄 전체를 추출하기
print(iphone_dataframe.loc[:, ["디스플레이", "메모리"]])
print("\n")
print(iphone_dataframe[["디스플레이", "메모리"]])
print("\n")
print(iphone_dataframe.loc[:, "메모리" : "Face ID" ])
print("\n")

#조건으로 row 추출하기
print(iphone_dataframe.loc[[True, False, True, False, True, True, False]])
print("\n")
print(iphone_dataframe.loc[(iphone_dataframe["디스플레이"] > 5) & (iphone_dataframe["Face ID"] == "Yes")])
print("\n")

#조건으로 column 추출하기
print(iphone_dataframe.loc[:, [True, True, False, False, False]])
print("\n")

#위치로 추출하기
print(iphone_dataframe.iloc[2, 4])
print("\n")
print(iphone_dataframe.iloc[[1, 3], [2, 4]])
print("\n")
print(iphone_dataframe.iloc[3:, 1:4])