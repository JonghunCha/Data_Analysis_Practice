import numpy

#numpy array각 요소에 boolean적용
array1 = numpy.array([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1])
print(array1 > 3)
print(array1 % 2 == 0)
print("\n")

#numpy.where과 boolean값을 이용하여 원하는 데이터의 위치 알아내기
boolean_array1 = array1 > 3
print(numpy.where(boolean_array1))
print("\n")

#이를 응용하여 조건에 맞는 데이터를 아래와 같이 추출할 수 있다
filter = numpy.where(array1 > 3)
print(array1[filter])