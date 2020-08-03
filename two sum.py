def twoNumberSum(array, targetSum):
	book = {}
    for (ele in array):
        match = targetSum - ele
        if match in book:
            return [book[match], match]
		elif ele in book:
			return [ele, book[ele]]
		else:
			book[match] = ele
	return []

