# 方法 a
def power2n_a(n):
    return 2**n

# 方法 b：用遞迴
def power2n_b(n):
    if n == 0: return 1
    return power2n_b(n-1)+power2n_b(n-1)

# 方法 c：用遞迴
def power2n_c(n):
    # pass
    if n == 0: return 1
    return 2*power2n_c(n-1)

# 方法 d：用遞迴+查表
def power2n_d(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 1
    result = power2n_d(n-1, memo) * 2
    memo[n] = result
    return result

print('power2n(40)=', power2n_c(40))