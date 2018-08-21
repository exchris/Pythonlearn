def average(*args):
	len1 = len(args)
	count = sum(args)
	if len1 == 0:
		return 0
	else:
		return count/len1

print(average(1,2,2,3,4))

def firstCharUpper(s):
	return s[0].upper()+s[1:]

print(firstCharUpper('hello'))
print(firstCharUpper('sunny'))
print(firstCharUpper('september'))