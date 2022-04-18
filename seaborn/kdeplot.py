"""
1. seaborn.kdeplot()의 경우 pandas.plot()과 다르게 정렬을 해주지 않아도 잘 나오는 것으로 보임
2. bw_method(혹은 bw_adjust)는 smoothing parameter로 값이 클수록 큰 너비에 대해, 값이 작을수록 좁은 너비에 대해 각각의 smoothing이 진행되는 것으로 보임
"""
import pandas
import seaborn
import matplotlib.pyplot

df = pandas.read_csv("data/body.csv", index_col=0)
print(df)
print("\n")

#키에 대해 KDE
seaborn.kdeplot(x=df["Height"])
matplotlib.pyplot.show()

#키에 대해 KDE(with bw=0.05)
seaborn.kdeplot(x=df["Height"], bw_method=0.05)
matplotlib.pyplot.show()

#키에 대해 KDE(with bw=0.5)
seaborn.kdeplot(x=df["Height"], bw_method=0.5)
matplotlib.pyplot.show()

#몸무게에 대해 KDE
seaborn.kdeplot(x=df["Weight"])
matplotlib.pyplot.show()

#키와 몸무게에 대한 KDE
#결과는 3차원의 KDE를 위에서 바라본 것이라 해석할 수 있다. 선간의 간격이 좁을수록 가파르고, 멀수록 완만하다(등고선과 같음)
seaborn.kdeplot(x=df["Height"], y=df["Weight"])
matplotlib.pyplot.show()

#histogram과 KDE를 동시에 표현
seaborn.histplot(x=df["Height"], kde=True, bins=15)
matplotlib.pyplot.show()

#boxplot과 KDE 동시에 표현
seaborn.violinplot(y=df["Height"])
matplotlib.pyplot.show()
