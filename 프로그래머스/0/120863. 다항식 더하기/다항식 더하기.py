def solution(polynomial):
    poly=polynomial.split(' + ')
    num=0
    tmp=0
    for i in poly:
        if i.isdigit():
            num+=int(i)
        elif i == 'x':
            tmp+=1
        else:
            arr=i.split('x')
            tmp+=int(arr[0])
            
    if num == 0: # 상수항이 없는 경우
        return f'{tmp}x' if tmp !=1 else f'x'
    elif tmp == 0: # 일차항만 있는 경우
        return str(num)
    else:
        return f'{tmp}x + {num}' if tmp !=1 else f'x + {num}'
        
            
            
    