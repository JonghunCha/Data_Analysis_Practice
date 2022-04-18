import pandas
import seaborn
import matplotlib.pyplot

df = pandas.read_csv("data/laptops.csv")
print(df)
print("\n")

#os별 laptop의 가격 그리기(비교방법 boxplot)
seaborn.catplot(data=df, x="os", y="price", kind="box")
matplotlib.pyplot.show()

#os별 laptop의 가격 그리기(비교방법 violin)
seaborn.catplot(data=df, x="os", y="price", kind="violin")
matplotlib.pyplot.show()

#os별 laptop의 가격 그리기(비교방법 strip)
seaborn.catplot(data=df, x="os", y="price", kind="strip")
matplotlib.pyplot.show()

#os별 laptop의 가격 그리기(비교방법 strip + processor_brand에 따라 색을 다르게 표현)
seaborn.catplot(data=df, x="os", y="price", kind="strip", hue="processor_brand")
matplotlib.pyplot.show()

#os별 laptop의 가격 그리기(비교방법 swarm + processor_brand에 따라 색을 다르게 표현)
#swarm을 사용하면 점들이 겹치지 않고 펼쳐서 그려진다
seaborn.catplot(data=df, x="os", y="price", kind="swarm", hue="processor_brand")
matplotlib.pyplot.show()