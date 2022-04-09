import pandas

#DataFrame생성 및 type, shape, size 확인
list = [["name1", 40, 70], ["name2", 50, 60], ["name3", 30, 90]]
dataframe1 = pandas.DataFrame(list)
print(dataframe1)
print(type(dataframe1))
print(dataframe1.shape)
print(dataframe1.size)
print("\n")

#DataFrame의 column과 row(pandas에서 index로 지정)에 이름 지정하기
dataframe2 = pandas.DataFrame(list, columns=["name", "age", "weight"], index=["a", "b", "c"])
print(dataframe2)
print(dataframe2.columns)
print(dataframe2.index)
print(dataframe2.dtypes)