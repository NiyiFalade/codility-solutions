import math


def solution(X, Y, D):

 distance =(Y-X)/D
 no_of_jmps = math.ceil(distance)

 return no_of_jmps


if __name__ == "__main__":
 
    assert solution(10,85,30) == 3
    assert solution(10, 70, 30) == 2
    assert solution(1, 5, 1) == 4
    assert solution(1, 1_000_000_000, 1) == 999_999_999
    assert solution(10, 31, 30) == 1
    print("All test cases passed!")
