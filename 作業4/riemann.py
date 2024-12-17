import numpy as np

# 定義被積分的函數
def integrand(x, y, z):
    return 3 * x**2 + y**2 + 2 * z**2

# 黎曼積分計算
def riemann_integration(n):
    dx = dy = dz = 1 / n  # 每個區間的寬度
    integral_sum = 0.0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                x = (i + 0.5) * dx  # 中心點近似
                y = (j + 0.5) * dy
                z = (k + 0.5) * dz
                integral_sum += integrand(x, y, z)
    
    return integral_sum * dx * dy * dz

# 設定分割數
n = 100
result_riemann = riemann_integration(n)
print(f"黎曼積分結果: {result_riemann}")
