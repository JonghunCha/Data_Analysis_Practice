import pandas

#read_csv()를 이용하여 csv파일을 읽어 DataFrame으로 저장
iphone_dataframe1 = pandas.read_csv("./iphone.csv")
print(iphone_dataframe1)
print(type(iphone_dataframe1))
print("\n")

#제품명을 DataFrame의 index로 사용하기
iphone_dataframe2 = pandas.read_csv("./iphone.csv", index_col=0)
print(iphone_dataframe2)

"""
주의 : pandas의 read_csv()는 csv파일의 첫 줄을 column의 이름으로 사용한다.
만약 csv의 첫 줄에 column의 이름이 없다면 아래와 같이 작성해야한다.
iphone_dataframe = pandas.read_csv("./iphone.csv", header=None)
"""