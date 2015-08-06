

Exercise 9-1

def display(f):
	result = []
	with open(f, 'r') as data:
		for line in data:
			if line[0] != '#':
				result.append(line)
	return result


def remove_comment(f):
	result = []
	with open(f, 'r') as data:
		for line in data:
			if line[0] != '#':
				if '#' in line:
					text, comment = line.split('#', 1)
					result.append(text)
				else:
					result.append(line)
	return result


Exercise 9-2

def display_line(f, n):
	i, result = 0, []
	with open(f, 'r') as data:
		for i in range(n):
			result.append((i+1, data.readline()))
	return result


Exercise 9-3

def wc_l(f):
	i = 0
	with open(f, 'r') as data:
		for line in data:
			i+=1
	return i


Exercise 9-4

def paper(f):
	result = []
	with open(f, 'r') as data:
		while True:
			command = raw_input('press a key to continue')
			if command == '':
				for i in range(25):
					result.append(data.readline())
				print '\n'.join(result)


Exercise 9-5

def score_list(f):
	result, scores, i = [], 0, 0
	g_dic = {'A': range(90, 101), 'B': range(80, 90), 'C': range(70, 80), 'D':range(60, 70), 'F':range(0, 60)}	
	with open(f, 'r') as data:
		for l in data:
		if num in nums:
			result.append(grades)
			scores+=num
			i+=1
	return result, scores/i


Exercise 9-
Exercise 9-
Exercise 9-
Exercise 9-
Exercise 9-
Exercise 9-
Exercise 9-
Exercise 9-
Exercise 9-
Exercise 9-
Exercise 9-
Exercise 9-
Exercise 9-
Exercise 9-
Exercise 9-