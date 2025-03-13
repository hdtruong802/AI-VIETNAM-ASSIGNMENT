# Tính tổng các chữ số của n
n = int(input("Nhập n: "))
o_n = n

s = 0
while n > 0:
	s += n % 10
	n //= 10

print(f"Tổng các chữ số của {o_n}: {s}")
print("-" * 60)

# Giải phương trình tìm nghiệm bằng phương pháp Newton: f(x) = x^3 - 3x + 1 = 0
x0 = 5 
e = 0.0001
x = 0
while True:
	x = x0 - (x ** 3 - 3 * x + 1) / (3 * (x ** 2) -3)
	if abs(x - x0) < e:
		break
	x0 = x

print(f"Nghiệm gần đúng của phương trình f(x) = x^3 - 3x + 1 = 0 là x = {x}")	
