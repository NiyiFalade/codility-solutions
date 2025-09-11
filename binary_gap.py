def solution(N):
    b = bin(N)[2:]
    currentGap = 0
    maxGap= 0

   

    for ch in b:
       if ch == '1':
          if currentGap > maxGap:
             maxGap = currentGap
             currentGap = 0 
       else:
          currentGap += 1
          
    return maxGap
             
       
          
def test_binary_gap():
    assert solution(9) == 2        # 1001 → gap of 2
    assert solution(529) == 4      # 1000010001 → longest gap 4
    assert solution(20) == 1       # 10100 → gap of 1
    assert solution(15) == 0       # 1111 → no gap
    assert solution(32) == 0       # 100000 → trailing zeros only
    assert solution(1041) == 5     # 10000010001 → longest gap 5
    assert solution(1) == 0        # 1 → no gap
    assert solution(6) == 0        # 110 → no gap
    print("All test cases passed!")       
          
      
          
       
          
    
   
    

if __name__ == "__main__":
 
 N = 529
 #print(solution(N))
 test_binary_gap()




