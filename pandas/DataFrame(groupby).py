import pandas
import matplotlib.pyplot

pandas.set_option("display.max_rows", None)
pandas.set_option("display.max_columns", None)

df = pandas.read_csv("data/laptops.csv")

#brand컬럼으로 group을 만들기
brand_groups = df.groupby("brand")
print(type(brand_groups))
print("\n")

#count(), mean()등의 함수 사용 가능
print(brand_groups.count())
print("\n")

#만약 특정 컬럼만의 mean()을 보고 싶은 경우
print(brand_groups.mean()[["clock_speed", "weight"]])
print("\n")

#plot으로 시각화도 가능
brand_groups.plot(kind="hist", y="price")
matplotlib.pyplot.show()