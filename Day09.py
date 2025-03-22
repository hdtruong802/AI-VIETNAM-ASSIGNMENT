# Bài 1: Áp dụng List 2D
matrix = []

for i in range(3):
	row = []
	for j in range(3):
		num = int(input(f"Nhập phần tử [{i}][{j}]:"))
		row.append(num)
	matrix.append(row)

print(f"Ma trận: {matrix}")
s = 0
for row in matrix:
	for element in row:
		s += element

print(f"Tổng các phần tử: {s}")
print("-" * 60)

# Bài 2: List Slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"List ban đầu: {numbers}")
print(f"Từ chỉ số 2 đến 6: {numbers[2:7]}")
print(f"Các số chẵn: {[i for i in numbers if i % 2 == 0]}")
print(f"List đảo ngược: {numbers[::-1]}")
print("-" * 60)

# Bài 3: Set và Tuple
my_list = [1, 2, 2, 3, 4, 4, 5]
print(f"List ban đầu: {my_list}")

my_set = set(my_list)
my_set.add(6)
print(f"Set sau khi loại trùng và thêm 6: {my_set}")

my_tuple = tuple(my_set)
print(f"Tuple: {my_tuple}")
print(f"Giá trị lớn nhất: {max(my_tuple)}")