# 条件判断

# 输入用户年龄,根据年龄打印不同的内容
age = input('Please enter your age :')
age = int(age);
if age >= 18 :
    print('your age is: %d' %age)
    print('adult')
elif age >= 6 :
    print('your age is: %d' %age)
    print('teenager')
else :
    print('kid')
