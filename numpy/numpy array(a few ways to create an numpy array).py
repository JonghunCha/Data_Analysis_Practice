import numpy

#1. 파이썬 리스트를 통해 생성
array1 = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
print(array1)
print("\n")

#2. 균일한 값으로 생성
array2 = numpy.full(3, 4)
print(array2)
print("\n")

#3. 모든 값이 0인 numpy array생성
array3 = numpy.full(5, 0)
array4 = numpy.zeros(5, dtype=int)
print(array3)
print(array4)
print("\n")

#4. 모든 값이 1인 numpy array생성
array5 = numpy.full(5, 1)
array6 = numpy.ones(5, dtype=int)
print(array5)
print(array6)
print("\n")

#5. 랜덤한 값들로 생성
array7 = numpy.random.random(5)
array8 = numpy.random.random(5)
print(array7)
print(array8)
print("\n")

#6. 연속된 값들이 담긴 numpy array 생성
array9 = numpy.arange(5)
array10 = numpy.arange(1, 6)
array11 = numpy.arange(1, 20, 2)
print(array9)
print(array10)
print(array11)