# Bài 1: Tạo danh sách số nguyên từ bàn phím
num = int(input("Nhập số lượng phần tử: "))
my_list = []
# my_list = [5, 2, 8, 1]

for i in range(num):
	n = int(input(f"Nhập số thứ {i+1}: "))
	my_list.append(n)

print(f"List: {my_list}")
print("-" * 60)

# Bài 2: Tính toán trên List
print(f"Tổng: {sum(my_list)}")
print(f"Giá trị lớn nhất: {max(my_list)}")
print(f"Giá trị nhỏ nhất: {min(my_list)}")
print("-" * 60)

# Bài 3: Thêm và xóa phần tử
numbers = [10, 20, 30, 40]
print(f"List ban đầu: {numbers}")

numbers.append(int(input("Nhập giá trị phần tử cần thêm: ")))
print(f"List sau khi thêm: {numbers}")

numbers.insert(int(input("Nhập vị trí chèn: ")), int(input("Nhập giá trị chèn: ")))
print(f"List sau khi chèn: {numbers}")

remove_number = int(input("Nhập giá trị xóa: "))
if remove_number in numbers:
	numbers.remove(remove_number)
	print(f"List sau khi xóa: {numbers}")
else:
	print(f"Không có giá trị {remove_number} trong list!")
	print(f"List sau khi xóa: {numbers}")
print("-" * 60)

# Bài 4: Duyệt list bằng vòng lặp
n = 0

print("Duyệt bằng for:")
for i in numbers:
    print(f"Phần tử tại chỉ số {numbers.index(i)} là {i}")

print("Duyệt bằng while:")
while n < len(numbers):
    print(f"Phần tử tại chỉ số {n} là {numbers[n]}")
    n += 1
print("-" * 60)

# Bài 5: Tìm kiếm phần tử trong list
s = int(input("Nhập một số: "))
if s in numbers:
	print(f"{s} có trong list, vị trí: {numbers.index(s)}")
else:
	print(f"Không tìm thấy {s} trong list!")