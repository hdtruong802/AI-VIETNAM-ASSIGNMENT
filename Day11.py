# Bài 1: Kiểm tra phần tử trùng lặp

nums = [1, 2, 3, 1]


def containsDuplicate(nums):
	count = {}
	result = False
	for num in nums:
		if num in count:
			count[num] += 1
			result = True
		else:
			count[num] = 1
	return result

print(containsDuplicate(nums))
print("-" * 60)

# Bài 2: Nhóm các chuỗi đảo chữ

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

def groupAnagrams(strs):
	result = []
	groups = []

	for word in strs:
		sorted_word = "".join(sorted(word))
		t = False

		for i in range(len(groups)):
			if groups[i] == sorted_word:
				result[i].append(word)
				t = True
				break

		if not t:
			groups.append(sorted_word)
			result.append([word])

	return result

print(groupAnagrams(strs))
print("-" * 60)

# Bài 3: Tìm cặp số có tổng bằng đích

nums = [2, 7, 11, 15]
target = 9

def twoSum(nums, target):
	for i in range(len(nums)):
		for j in range(i+1, len(nums)):
			if target == nums[i] + nums[j]:
				return [i, j]

print(twoSum(nums, target))