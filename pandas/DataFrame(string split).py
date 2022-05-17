import pandas

pandas.set_option("display.max_rows", None)
pandas.set_option("display.max_columns", None)

df = pandas.read_csv("data/parks.csv")

#띄어쓰기로 문자열 분리
print(df["소재지도로명주소"].str.split())
print("\n")

#분리된 문자열에서 n번째 공백까지 분리
print(df["소재지도로명주소"].str.split(n=2))
print("\n")

#분리한 결과를 새로운 DataFrame으로 반환
print(df["소재지도로명주소"].str.split(n=2, expand=True))
print("\n")

#기존 df에 추출하고자 하는 정보를 추가
address = df["소재지도로명주소"].str.split(n=2, expand=True)
df["관할구역"] = address[0]
print(df)