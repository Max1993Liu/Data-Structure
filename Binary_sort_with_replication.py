def binary_search(s, target, left = 0, right = None):
	if right is None:
		right = len(s)
	mid = (left + right) //2
	if s[mid] == target:
		ret = [mid]
		i = 1
		while mid - i >= 0 and s[mid - i]== target:
			ret.append(mid - i)
			i += 1
		i = 1
		while mid + i < len(s) and s[mid + i] == target:
			ret.append(mid + i)
			i += 1
		return sorted(ret)
	elif s[mid] < target:
		return binary_search(s, target, mid + 1, right)
	else:
		return binary_search(s, target, left, mid)

