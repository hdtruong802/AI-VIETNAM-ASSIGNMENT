N = int(input("Nhập N: "))

# Tìm tất cả các số nguyên tố trong khoảng từ 1 đến N
def find_primes(N):
	primes = []
	for i in range(2, N + 1):
		t = True
		for j in range(2, int(i ** 0.5) + 1):
			if i % j == 0:
				t = False
				break
		if t:
			primes.append(i)
	return primes

result = find_primes(N)
print(f"Các số nguyên tố trong khoảng từ 1 đến {N}: {result}")
print("-" * 60)

# Tính tổng các số hoàn hảo nhỏ hơn N
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

		return sum(perfect_numbers), perfect_numbers
	else:
		return 0


result, perfect_numbers = sum_perfect_numbers(N)
print(f"Tổng các số hoàn hảo nhỏ hơn {N}: {result} ({', '.join(map(str, perfect_numbers))})")
