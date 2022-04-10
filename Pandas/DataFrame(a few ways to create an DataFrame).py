import numpy
import pandas

#1. python list, numpy array, pandas seried로부터 생성
list = [["name1", 40, 70], ["name2", 50, 60], ["name3", 30, 90]]
narray = numpy.array(list)
list_of_series = [
    pandas.Series(["name1", 40, 70]),
    pandas.Series(["name2", 50, 60]),
    pandas.Series(["name3", 30, 90])
]

dataframe1 = pandas.DataFrame(list)
dataframe2 = pandas.DataFrame(narray)
dataframe3 = pandas.DataFrame(list_of_series)
print(dataframe1)
print(dataframe2)
print(dataframe3)
print("\n")

#2. python list 담긴 python dictionary로부터 생성
name = ["name1", "name2", "name3"]
age = [40, 50, 30]
weight = [70, 60, 90]

dict1 = {
    "name" : name,
    "age" : age,
    "weight" : weight
}
dict2 = {
    "name" : numpy.array(name),
    "age" : numpy.array(age),
    "weight" : numpy.array(weight)
}
dict3 = {
    "name" : pandas.Series(name),
    "age" : pandas.Series(age),
    "weight" : pandas.Series(weight)
}

dataframe1 = pandas.DataFrame(dict1)
dataframe2 = pandas.DataFrame(dict2)
dataframe3 = pandas.DataFrame(dict3)

print(dataframe1)
print(dataframe2)
print(dataframe3)
print("\n")

#3. python dictionary가 담긴 python list로부터 생성
list = [
    {"name" : "name1", "age" : 40, "weight" : 70},
    {"name" : "name2", "age" : 50, "weight" : 60},
    {"name" : "name3", "age" : 30, "weight" : 90}
]

dataframe1 = pandas.DataFrame(list)

print(dataframe1)