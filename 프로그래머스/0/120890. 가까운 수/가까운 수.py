def solution(array, n):
    array=sorted(array)
    gap=100
    max_num=n
    for i in array:
        if gap>abs(n-i):
            gap=abs(n-i)
            max_num=i
    return max_num