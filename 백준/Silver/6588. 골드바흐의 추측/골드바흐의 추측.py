import sys
# 에라토스테네스의 체로 소수 리스트 만들기
is_prime = [True] * (1000000 + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, 1001):
    if is_prime[i]:
        for j in range(i * i, 1000000+1, i):
            is_prime[j] = False
def get_goldbach(n):
    # 두 소수의 합으로 표현하기
    for i in range(2, n // 2 + 1):
        if is_prime[i] and is_prime[n - i]:
            return i, n - i
    return None
while True:
    n=int(sys.stdin.readline())
    if n == 0:
        break
    result = get_goldbach(n)
    if not result:
        print("Goldbach's conjecture is wrong.")
    else:
        print(f"{n} = {result[0]} + {result[1]}")