import numpy

#numpy array도 파이썬 리스트처럼 인덱스를 통해 접근 가능하다
array1 = numpy.array([1, 2, 3, 4, 5, 6, 7, 8])
print(array1[0])
print(array1[3])
print(array1[-1])
print(array1[-3])
print(array1[[1, 3, 5]])

#numpy array를 numpy array의 인덱스로 사용할 수 있다
array2 = numpy.array([2, 4, 6])
print(array1[array2])

#numpy array도 파이썬 리스트처럼 슬라이싱이 가능하다
print(array1[3:5])
print(array1[:7])
print(array1[4:])
print(array1[3:-2])
print(array1[0:8:2])