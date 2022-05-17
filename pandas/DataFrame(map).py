"""
map은 각 데이터를 매핑된 다른 값으로 변환하는 역할을 수행한다
"""
import pandas

df = pandas.read_csv("data/laptops.csv")

#각 제조사와 그 제조사의 국가를 매핑한 자료
brand_nation = {
    "Dell" : "U.S.",
    "Apple" : "U.S.",
    "Acer" : "Taiwan",
    "HP" : "U.S.",
    "Lenovo" : "China",
    "Alienware" : "U.S.",
    "Microsoft" : "U.S.",
    "Asus" : "Taiwan"
}

#brand컬럼의 제조사를 나라로 매핑한 결과를 brand_nation이라는 컬럼명으로 추가
df["brand_nation"] = df["brand"].map(brand_nation)
print(df)