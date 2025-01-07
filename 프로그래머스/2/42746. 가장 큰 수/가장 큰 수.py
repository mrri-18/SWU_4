def solution(numbers):
    numbers = list(map(str, numbers))
    
    # 정렬 기준: x+y와 y+x를 비교
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    return str(int(''.join(numbers)))
            
