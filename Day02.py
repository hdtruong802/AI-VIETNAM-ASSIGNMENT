def score(student_name, math_score, science_score):
	print(f"Tên: {student_name}, Điểm Toán: {math_score}, Điểm Khoa học: {science_score}")
	# print("Tên: " + student_name + ", Điểm Toán: " + str(math_score) + ", Điểm Khoa học: " + str(science_score))
	print(f"Tổng điểm: {math_score + science_score}")
	print(f"Hiệu điểm: {math_score - science_score}")
	print(f"Tích điểm: {math_score * science_score}")
	print(f"Thương điểm: {math_score / science_score}")

	# Điểm trung bình
	avg_score = (math_score + science_score) / 2
	if avg_score >= 8.0:
		print("Xuất sắc")
	elif 8.0 > avg_score >= 6.5:
		print("Khá")
	elif 6.5 > avg_score >= 5.0:
		print("Trung bình")
	else:
		pass

math_score = 8.5 + 1.0
science_score = 7.0

score("An", math_score, science_score)
