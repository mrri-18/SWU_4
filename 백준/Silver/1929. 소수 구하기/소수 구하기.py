import sys

def get_prime_numbers(m,n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:  # i가 소수인 경우
            # i의 배수들을 모두 소수가 아닌 것으로 표시
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    # 소수인 숫자들만 리스트로 반환
    prime_numbers = [i for i in range(m, n + 1) if is_prime[i]]
    return prime_numbers
m,n=map(int,sys.stdin.readline().split())
for i in get_prime_numbers(m,n):
    print(i)