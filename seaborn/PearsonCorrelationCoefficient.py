import pandas
import seaborn
import matplotlib.pyplot

df = pandas.read_csv("data/exam.csv")
print(df)
print("\n")

#exam의 상관계수를 나타내는 DataFrame출력
print(df.corr())
print("\n")

#상관계수를 seaborn의 heatmap()을 이용하여 시각화
seaborn.heatmap(df.corr())
matplotlib.pyplot.show()

#heatmap에 상관계수를 나타내는 수도 표시
seaborn.heatmap(df.corr(), annot=True)
matplotlib.pyplot.show()