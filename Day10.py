# Bài 1: Quản lý danh sách môn học

subjects = [("Toán", 3, 8.5), ("Lý", 2, 7.0), ("Hóa", 3, 9.0)]

credits = []
scores = []
high_tup = ()
highest_score = 0
for subject in subjects:
	credits.append(subject[1])
	scores.append(subject[2])

	if subject[2] > highest_score:
		highest_score = subject[2]
		high_tup = subject

count_credit = {}
for credit in credits:
	if credit in count_credit:
		count_credit[credit] += 1
	else:
		count_credit[credit] = 1

print(f"Từ điển số tín chỉ: {dict(sorted(count_credit.items()))}")
print(f"Tập hợp điểm TB: {set(scores)}")
print(f"Môn học cao nhất: {high_tup}")
print("-" * 60)

# Bài 2: Phân loại số theo tần suất

numbers = [1, 2, 2, 3, 1, 4]

count_num = {}
once_num = []
for num in numbers:
	if num in count_num:
		count_num[num] += 1
		once_num.remove(num)
	else:
		count_num[num] = 1
		once_num.append(num)

print(f"Từ điển tần suất: {count_num}")
print(f"Tập hợp số xuất hiện 1 lần: {set(once_num)}")
print(f"Danh sách sắp xếp: {tuple(sorted(count_num.items()))}")
print("-" * 60)

# Bài 3: Tìm cặp giá trị gần nhất
pairs = [(10, 0), (15, 1), (13, 2), (12, 3)]
differences = []
values = []

for i in range(len(pairs)):
	for j in range(i + 1, len(pairs)):
		dif = abs(pairs[i][0] - pairs[j][0])
		differences.append(((pairs[i][1], pairs[j][1]),dif))

min_diff = differences[0][1]

for diff in differences:
	if min_diff > diff[1]:
		min_diff = diff[1]
		min_diff_pair = diff[0]

for pair in pairs:
	values.append(pair[0])

print(f"Cặp chỉ số gần nhất: {min_diff_pair}")
print(f"Từ điển chênh lệch: {dict(differences)}")
print(f"Tập hợp giá trị: {set(values)}")
