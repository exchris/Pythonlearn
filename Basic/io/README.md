### 操作文件和目录
- 获得当前Python脚本工作的目录路径: os.getcwd()
- 返回指定目录下的所有文件和目录名: os.listdir()。例如返回C盘下的文件: os.listdir("C:\\")
- 删除一个文件: os.remove(filepath)
- 删除多个空目录: os.removedirs(r"d:\python")
- 检验给出的路径是否是一个文件: os.path.isfile(filepath)
- 检验给出的路径是否是一个目录: os.path.isdir(filepath)
- 判断是否是绝对路径: os.path.isabs()
- 检验路径是否真的存在: os.path.exists()。例如检验D盘下是否有Python文件夹:os.path.exists(r"d:\python")
- 分离一个路径的目录名和文件名:os.path.split()。例如:
os.path.split(r"/home/qiye/qiye.txt"),返回结果的是一个元组:('/home/qiye', 'qiye.txt')
