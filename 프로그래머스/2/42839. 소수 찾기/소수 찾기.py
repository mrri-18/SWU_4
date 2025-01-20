from itertools import permutations
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # 루트 N까지 확인
        if n % i == 0:
            return False
    return True
def solution(numbers):
    answer = 0
    unique_numbers = set()
    for i in range(1,len(numbers)+1):
        for j in list(permutations(numbers,i)):
            unique_numbers.add(int(''.join(j)))    
                               
    for num in unique_numbers: #소수 판별                      
        if is_prime(num):
            answer += 1
    return answer