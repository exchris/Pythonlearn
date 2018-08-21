try:
    file = open(r'd:\qiye.txt', 'r')
    print(file.read())
finally:
    file.close()

#
# with open(r'd:\qiye.txt', 'r') as fileReader:
#    print(fileReader.read())
#

with open(r'd:\qiye.txt', 'r') as fileReader:
    for line in fileReader.readlines():
        print(line.strip())

# 文件写入
f = open(r'd:\qiye.txt', 'w')
f.write('qiye')
f.close()