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

#column 두 줄 전체를 추출하기
print(iphone_dataframe.loc[:, ["디스플레이", "메모리"]])
print("\n")
print(iphone_dataframe[["디스플레이", "메모리"]])