import pandas
import matplotlib.pyplot

df = pandas.read_csv("./data/body.csv")
print(df)
print("\n")

#키의 분포에 대해 히스토그램 그리기
df.plot(kind="hist", y="Height")
matplotlib.pyplot.show()

#범위의 갯수를 지정하고 싶을 때
df.plot(kind="hist", y="Height", bins=15)
matplotlib.pyplot.show()