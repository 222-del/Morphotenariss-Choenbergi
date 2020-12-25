def solution(n):
    if n == 0 or n == 1:
        return 1
    elif n % 2 == 0:
        return solution(n / 2) + 1
    else:
        return solution(n + 1) + solution((n - 1) / 2)

print(solution(5))
