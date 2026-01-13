def solution(numbers):
    numbers = list(map(str, numbers))
    
    numbers.sort(key=lambda x: x*3, reverse=True) # int 비교 x
    
    return str(int(''.join(numbers)))