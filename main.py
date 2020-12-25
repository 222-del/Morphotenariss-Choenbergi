def func(nums):
    max = 1
    for i in range(len(nums)):
        nmax = 1
        c = nums[i]
        for j in range(len(nums) - i):
            if (c == nums[j + i]):
                nmax += 1
        if (nmax > max):
            max = nmax
    return max


def solution(nums):
    max = func(nums)
    min = len(nums)
    tmin = min
    for i in range(len(nums)):
        t = nums[0:i + 1]
        if (func(t) == max):
            tmin = len(t)
    if (tmin < min):
        min = tmin
    for i in range(len(nums)):
        t = nums[-i:]
        if (func(t) == max):
            tmin = len(t)
    if (tmin < min):
        min = tmin
    return (min)


a = [1, 2, 2, 3, 1, 4, 2]
print(solution(a))
