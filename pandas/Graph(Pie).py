"""
1. 파이 그래프는 index를 기준으로 이름표를 붙인다. 따라서 원하는 라벨이 있다면, set_index()로 바꿔줘야한다.
"""
import pandas
import matplotlib.pyplot

df = pandas.read_csv("data/broadcast.csv", index_col=0)
print(df)
print("\n")

#2017년 각 방송사의 시청률을 파이 그래프로 그리기
df.loc[2017].plot(kind="pie")
matplotlib.pyplot.show()