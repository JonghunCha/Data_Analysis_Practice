numpy에 대해 공부하며 작성한 예제 코드들입니다.

# 1. numpy array vs python list
    문법 차이 1

    numpy array
    [1, 2, 3, 4, 5] + [1, 2,3, 4, 5] = [2, 4, 6, 8, 10]
    
    python list
    [1, 2, 3, 4, 5] + [1, 2, 3, 4, 5] = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

    덧셈의 경우 위와 같은 차이가 있다.  
    또한 뺄셈, 곱셈, 나눗셈의 경우 numpy array에서는 덧셈처럼 각 인덱스에 해당하는 값끼리 연산이 가능하지만  
    python list에서는 위와 같은 명령은 오류를 일으킨다.
***
    문법 차이 2

    numpy array
    [1, 2, 3, 4, 5] + 5 = [6, 7, 8, 9, 10]

    python list
    [1, 2, 3, 4, 5] + 5 = 오류

    numpy array에 특정 값을 덧셈, 뺄셈, 나눗셈을 하면 각 인덱스에 해당하는 값에 연산이 일어난다.
    그러나 python list에서는 덧셋, 뺄셈, 나눗셈에 대하여 오류를 일으킨다.

    numpy array
    [1, 2, 3, 4, 5] * 2 = [2, 4, 6, 8, 10]

    python list
    [1, 2, 3, 4, 5] * 2 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    
    곱셈의 경우 numpy array는 각 요소의 값에 곱셈을 한다면 python list는 각 요소를 곱하는 횟수만큼 반복하여 이어붙인다.
***
    성능 차이
    
    numpy array가 python list보다 계산 속도 측면에서 훨씬 빠르다.

    하나의 numpy array안에는 동일한 타입의 데이터만 저장할 수 있다.
    반대로 하나의 python list에는 여러가지 타입의 데이터를 섞어서 저장할 수 있다.

    저장된 데이터의 타입이 같다는 것은 각 데이터가 필요로 하는 저장공간이 같다는 것을 의미하고,
    이는 n번째 데이터에 빠르게 접근할 수 있게 만든다.