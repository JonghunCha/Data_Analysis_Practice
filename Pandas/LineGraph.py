import pandas
import matplotlib.pyplot

df = pandas.read_csv("data/broadcast.csv", index_col=0)
print(df)
print("\n")

#모든 방송사에 대해 선 그래프 그리기
df.plot(kind="line")
matplotlib.pyplot.show()

#KBS에 대해서만 선 그래프 그리기
df.plot(kind="line", y="KBS")
matplotlib.pyplot.show()

#KBS, MBC, SBS에 대해 선 그래프 그리기
df.plot(kind="line", y=["KBS", "MBC", "SBS"])
matplotlib.pyplot.show()
df[["KBS", "MBC", "SBS"]].plot(kind="line")
matplotlib.pyplot.show()