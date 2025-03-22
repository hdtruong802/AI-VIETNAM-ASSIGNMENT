import math

# Tính giai thừa
def factorial(n):
    if n < 0:
        raise ValueError("Integer must be non-negative")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

n = 6
print(f"Giai thừa của {n} là: {factorial(n)}")
print("-" * 60)


# Tính số e bằng chuỗi Taylor
def calculate_e(n):
    return sum(1 / factorial(i) for i in range(n))

n = 8
e_approx = calculate_e(n)
print(f"Số e gần đúng với {n} số hạng: {e_approx}")
print(f"Số e thực tế: {math.e}")
print(f"Độ lệch: {abs(math.e - e_approx)}")
print("-" * 60)


# Tính e^x bằng chuỗi Taylor
def calculate_exp(x, n):
    return sum((x ** i) / factorial(i) for i in range(n))

x = 2
n = 10
exp_approx = calculate_exp(x, n)
print(f"e^{x} gần đúng với {n} số hạng: {exp_approx}")
print(f"e^{x} thực tế: {math.exp(x)}")
print(f"Độ lệch: {abs(math.exp(x) - exp_approx)}")