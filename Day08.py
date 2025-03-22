import copy

# Bài 1: List Comprehension
n = int(input("Nhập n: "))
new_list = [i for i in range(n+1) if i % 2 != 0]
print(f"Danh sách số lẻ: {new_list}")
print("-" * 60)

# Bài 2: Copy List & Aliasing
original = [1, 2, [3, 4]]
print(f"Original ban đầu: {original}")

shallow_copy = original.copy()
print(f"Shallow copy ban đầu: {shallow_copy}")
deep_copy = copy.deepcopy(original)
print(f"Deep copy ban đầu: {deep_copy}")

shallow_copy[2][0] = 10
deep_copy[2][0] = 20
print(f"Shallow copy sau khi sửa: {shallow_copy}")
print(f"Deep copy sau khi sửa: {deep_copy}")
print(f"Original sau khi sửa: {original}")
print("-" * 60)

# Bài 3: Dictionary
students = {"An": 8.5, "Bình": 7.0}
new_student = input("Nhập tên học sinh: ")
new_score = float(input("Nhập điểm: "))
students[new_student] = new_score
print(f"Dictionary sau khi thêm: {students}")
print(f"Danh sách học sinh: {students.keys()}")

values = students.values()
avg = round(sum(values) / len(values), 2) # làm tròn 2 chữ số phần thập phân
print(f"Điểm trung bình: {avg}")