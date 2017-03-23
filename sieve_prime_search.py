def prime_list(upper_limit):
	divisor_list = [2,3]
	original_length = 2
	while divisor_list[-1] < upper_limit:
		if divisor_list[-1] ** 2 <= upper_limit:
			divisor_list.extend(range(divisor_list[-1] + 1, divisor_list[-1]**2))
			for i in range(original_length, len(divisor_list)):
				for j in range(original_length):
					if divisor_list[i] % divisor_list[j] == 0:
						divisor_list[i] = None
						break
			divisor_list = [i for i in divisor_list if i is not None]
			original_length = len(divisor_list)
		else:
			divisor_list.extend(range(divisor_list[-1] + 1, upper_limit))
			for i in range(original_length , len(divisor_list)):
				for j in range(original_length):
					if divisor_list[i] % divisor_list[j] == 0:
						divisor_list[i] = None
						break
			divisor_list = [i for i in divisor_list if i is not None]
			return divisor_list

t = prime_list(10)
print t