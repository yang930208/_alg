import numpy as np

# 定義被積分的函數
def integrand(x, y, z):
    return 3 * x**2 + y**2 + 2 * z**2

# 蒙地卡羅積分計算
def monte_carlo_integration(n):
    random_samples = np.random.rand(n, 3)  # 生成 n 組隨機點 (x, y, z)
    x_samples = random_samples[:, 0]
    y_samples = random_samples[:, 1]
    z_samples = random_samples[:, 2]
    
    # 計算函數值
    integral_sum = np.mean(integrand(x_samples, y_samples, z_samples))
    
    return integral_sum

# 設定抽樣數量
n = 100000
result_monte_carlo = monte_carlo_integration(n)
print(f"蒙地卡羅法積分結果: {result_monte_carlo}")
