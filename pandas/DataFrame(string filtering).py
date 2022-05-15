import pandas

pandas.set_option("display.max_rows", None)
pandas.set_option("display.max_columns", None)

df = pandas.read_csv("data/albums.csv")

#Genre가 Blues인 row 추출
print(df[df["Genre"] == "Blues"])
print("\n")

#Genre에 Blues를 포함한 row 추출
print(df[df["Genre"].str.contains("Blues")])
print("\n")

#Genre가 Blues로 시작하는 row 추출
print(df[df["Genre"].str.startswith("Blues")])
print("\n")
