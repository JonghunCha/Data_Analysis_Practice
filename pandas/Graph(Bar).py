import pandas
import matplotlib.pyplot

df = pandas.read_csv("data/sports.csv", index_col=0)
print(df)
print("\n")

#모든 종목에 대해 남성과 여성의 선호 비율 막대 그래프로 그리기
df.plot(kind="bar")
matplotlib.pyplot.show()

#막대를 가로로 그리기
df.plot(kind="barh")
matplotlib.pyplot.show()

#막대를 쌓아 올려 그리기
df.plot(kind="bar", stacked=True)
matplotlib.pyplot.show()

#하나의 column에 대해서만 그래프 그리기
df["Female"].plot(kind="bar")
matplotlib.pyplot.show()