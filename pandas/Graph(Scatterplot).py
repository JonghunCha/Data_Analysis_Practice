import pandas
import matplotlib.pyplot

df = pandas.read_csv("./data/exam.csv")
print(df)
print("\n")

#수학점수와 읽기점수 간의 scatter plot 그리기
df.plot(kind="scatter", x="math score", y="reading score")
matplotlib.pyplot.show()

#수학점수와 쓰기점수간의 scatter plot 그리기
df.plot(kind="scatter", x="math score", y="writing score")
matplotlib.pyplot.show()

#읽기점수와 쓰기점수간의 scatter plot 그리기
df.plot(kind="scatter", x="reading score", y="writing score")
matplotlib.pyplot.show()