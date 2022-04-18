import pandas
import seaborn
import matplotlib.pyplot

df = pandas.read_csv("data/body.csv", index_col=0)
print(df)
print("\n")

#scatterplot 위에 regression line그리기
seaborn.lmplot(data=df, x="Height", y="Weight")
matplotlib.pyplot.show() 