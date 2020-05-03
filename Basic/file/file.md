### 3.2.1 使用python读/写文本文件

open 打开一个文件并创建一个对象

使用python打开文件

- 第一种方式
```python
f = open('文件路径', '文件操作方式', encoding='utf-8')

# 对文件进行操作
f.close()
```

- 第二种方式
```python
with open('文件路径', '文件操作方式', encoding='utf-8') as f:
    # 对文件进行操作
    f.close()
```

**2.使用Python写文本文件**

```python
with open('new.txt', 'w', encoding='utf-8') as f:
    # 通过f来写文件
    # 直接将一大段字符串写入到文本中
    f.write('一大段文字')
    # 把列表里面的所有字符串写入到文本中
    f.writelines(['第一段话', '第二段话', '第三段话'])

```