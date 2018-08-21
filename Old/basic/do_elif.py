weight = 87.5
height = 1.75
bmi = weight/(height*height)
bmi = float ('%.1f' % bmi)
print('小明的bmi指数为',bmi)
if bmi < 18.5:
    print('过轻')
elif bmi < 25 :
    print('正常')
elif bmi < 28 :
    print('过重')
elif bmi < 32 :
    print('肥胖')
else :
    print('严重肥胖')
