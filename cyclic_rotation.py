def solution(A,k):
    if k == 0:
       return A
    

    if not isinstance(k, int):
     raise TypeError("k must be an integer")
    else :        
     rotated_i = []
    
     for i in range(1, k+1):
      rotated_i = A[-i:] + A[:-i]
      
    return rotated_i





if __name__ == "__main__":
 # 1. Basic rotation by 1
    print("Test 1:", solution([1, 2, 3, 4, 5], 1))  
    # Expected: [5, 1, 2, 3, 4]

    # 2. Rotate by 2
    print("Test 2:", solution([1, 2, 3, 4, 5], 2))  
    # Expected: [4, 5, 1, 2, 3]

    # 3. Rotate by 0 (should return original list)
    print("Test 3:", solution([1, 2, 3, 4, 5], 0))  
    # Expected: [1, 2, 3, 4, 5]

    # 4. Rotate by list length (should return original list)
    print("Test 4:", solution([1, 2, 3, 4, 5], 5))  
    # Expected: [1, 2, 3, 4, 5]

    # 5. Rotate more than list length
    print("Test 5:", solution([1, 2, 3, 4, 5], 7))  
    # Expected: [4, 5, 1, 2, 3]

    # 6. Single element list
    print("Test 6:", solution([42], 3))  
    # Expected: [42]

    # 7. Empty list
    print("Test 7:", solution([], 3))  
    # Expected: []