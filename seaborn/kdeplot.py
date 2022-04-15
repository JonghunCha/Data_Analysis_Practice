import pandas
import seaborn
import matplotlib.pyplot

df = pandas.read_csv("data/body.csv", index_col=0)
print(df)
print("\n")
print(seaborn.__version__)

#키에 대해 KDE
seaborn.kdeplot(df["Height"])
matplotlib.pyplot.show()

#키에 대해 KDE(with bw=0.05)
seaborn.kdeplot(df["Height"], bw=0.05)
matplotlib.pyplot.show()

#키에 대해 KDE(with bw=0.5)
seaborn.kdeplot(df["Height"], bw=0.5)
matplotlib.pyplot.show()

"""
1. seaborn.kdeplot()의 경우 pandas.plot()과 다르게 정렬을 해주지 않아도 잘 나오는 것으로 보임
2. bw(bandwidth)는 smoothing parameter로 bw가 커질수록 큰 너비에 대해, bw가 작을수록 좁은 너비에 대해 각각의 smoothing이 진행되는 것으로 보임
"""