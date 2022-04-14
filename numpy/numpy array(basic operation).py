import numpy

array1 = numpy.arange(10)
array2 = numpy.arange(10, 20)
print(array1)
print(array2)
print("\n")

#array1의 모든 값에 2를 곱하기, 나누기, 더하기, 빼기, 제곱한 결과 출력하기
print(array1 * 2)
print(array1 / 2)
print(array1 + 2)
print(array1 - 2)
print(array1 ** 2)
print("\n")

#numpy array끼리의 연산도 가능
print(array1 * array2)
print(array1 / array2)
print(array1 + array2)
print(array1 - array2)
print(array1 ** array2) #뒷 부분은 overflow가 나서 잘못된 값이 출력됨