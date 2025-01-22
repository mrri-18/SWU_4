import sys

def next_permutation(array):
    n = len(array)
    i = n - 1
    while i > 0 and array[i - 1] <= array[i]:
        i -= 1
    if i <= 0:
        return False    
    j = n - 1
    while array[j] >= array[i - 1]:
        j -= 1
    array[i - 1], array[j] = array[j], array[i - 1]  # swap

    # 뒷부분을 오름차순으로 정렬
    array[i:] = array[i:][::-1]
    return True

n = int(sys.stdin.readline().strip())
pre_dict = list(map(int, sys.stdin.readline().split()))

if next_permutation(pre_dict):
    print(' '.join(map(str, pre_dict)))
else:
    print(-1)