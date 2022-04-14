import pandas
import matplotlib.pyplot

df = pandas.read_csv("./data/exam.csv")
print(df)
print("\n")

#수학 점수 통계정보 확인
print(df["math score"].describe())
print("\n")

#수학 점수 박스 플롯 그리기
df.plot(kind="box", y="math score")
matplotlib.pyplot.show()

#여러 개의 박스 플롯 동시에 그리기
df.plot(kind="box", y=["math score", "reading score", "writing score"])
matplotlib.pyplot.show()