import pandas

liverpool_dataframe = pandas.read_csv("./liverpool.csv", index_col=0)
print(liverpool_dataframe)
print("\n")

#컬럼 이름 변경하기
liverpool_dataframe.rename(columns={"position":"Position", "born":"Born", "number":"Number", "nationality":"Nationality"}, inplace=True)
print(liverpool_dataframe)
print("\n")

#인덱스의 이름 지정하기
liverpool_dataframe.index.name = "Player Name"
print(liverpool_dataframe)
print("\n")

#인덱스 자체를 바꾸기(기존 인덱스를 새로운 column으로 추가한 뒤 set_index로 인덱스 바꾸기)
liverpool_dataframe["Player Name"] = liverpool_dataframe.index
liverpool_dataframe.set_index("Number", inplace=True)
print(liverpool_dataframe)
print("\n")