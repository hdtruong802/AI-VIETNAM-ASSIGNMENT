def sum_perfect_numbers(N):
    if N >= 2:
        perfect_numbers = []
        for num in range(2, N):
            divisors = []
            for i in range(1, num):
                if num % i == 0:
                    divisors.append(i)
            if sum(divisors) == num:
                perfect_numbers.append(num)
        
        return sum(perfect_numbers)
    else:
        return 0

# Nhập giá trị N từ người dùng
# N = int(input("Nhập N: "))
N = 30
result = sum_perfect_numbers(N)
print(f"Tổng các số hoàn hảo nhỏ hơn {N}: {result}")