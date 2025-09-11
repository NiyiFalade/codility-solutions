def solution(A):
    if type(A) is not list:
       return 'A is not list'
   
    B = set()   
    
    for i in range(len(A)):
       if A[i] not in B:
          B.add(A[i])
       else:
          B.remove(A[i])  
    return list(B)[0]  
          





if __name__ == "__main__":
 
   # 1. Input not a list
    assert solution("hello") == 'A is not list'

    # 2. Single element
    assert solution([7]) == 7

    # 3. Odd occurrence simple
    assert solution([1, 2, 2, 1, 3]) == 3

    # 4. Odd element in the middle
    assert solution([4, 4, 5, 6, 6]) == 5

    # 5. All same element odd times
    assert solution([9, 9, 9, 9, 9]) == 9

    # 6. Negative numbers
    assert solution([-1, -1, -2]) == -2

    # 7. Zeros included
    assert solution([0, 0, 7, 7, 7]) == 7

    # 8. Multiple pairs + one odd
    assert solution([10, 10, 20, 20, 30, 30, 30]) == 30

    # 9. Large input (performance test)
    large_test = [2]*1000000 + [3]
    assert solution(large_test) == 3

    print("All test cases passed!")
