import numpy

array1 = numpy.array([4, 2, 1, 3, 5])

#최댓값, 최솟값 찾기
print(array1.max())
print(array1.min())
print("\n")

#평균값, 중앙값 찾기
print(array1.mean())
print(numpy.median(array1)) #median()은 numpy array의 메소드가 아니라 numpy의 메소드다
print("\n")

#표준편차, 분산 찾기
print(array1.std())
print(array1.var())