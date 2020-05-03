### turtle库

画布

常用的画布方法

- screensize() 方法

```bash
语法：turtle.screensize(canvwidth=None,canvheight=None,bg=None)
canvwidth -- 宽
canvheight -- 高
bg -- 背景颜色
```

示例:
```python
import turtle, time
turtle.screensize(800, 600, "green")
turtle.screensize() #返回默认大小(400, 300)
time.sleep(3)
```

- setup()方法

```bash
语法：turtle.setup(width=0.5, height=0.75, startx=None, starty=None)
width、height  --  输入宽和高为整数时, 表示像素。为小数时, 表示占据电脑屏幕的比例 
startx、starty -- 这一坐标表示 矩形窗口左上角顶点的位置，如果为空，则窗口位于屏幕中心
```

**示例**
```python
import turtle, time
turtle.screensize(800, 600, "green")
turtle.screensize() #返回默认大小(400, 300)
time.sleep(3)
```

画笔

画笔有颜色、画线的宽度等属性

- turtle.pensize()：设置画笔的宽度
- turtle.pencolor()：没有参数传入返回当前画笔颜色，传入传入参数设置画笔颜色，可以是字符串如"red"、"blue"，也可以是RGB 3元组
- turtle.speed(): 设置画笔移动速度，画笔绘制的速度范围[0,10]整数，数字越大越快

绘画命令

操纵海龟绘图有多种命令，这些命令可以分为3中，分别是：画笔运动命令、画笔控制命令和全局控制命令

画笔运动命令

|命令|说明|
|:------:|:------:|
|turtle.forward(distance) | 向当前画笔方向移动distance像素长|
|turtle.backward(distance) | 向当前画笔相反方向移动distance像素长度|
|turtle.right(degree) | 顺时针移动degree°|
|turtle.left(degree) | 逆时针移动degree°|
|turtle.pendown()|移动时绘制图形，缺省时也会绘制|
|turtle.goto(x,y) |	将画笔移动到坐标为x，y的位置|
|turtle.penup()	|移动时不绘制图形,提起笔，用于另起一个地方绘制时用|
|turtle.speed(speed)|	画笔绘制的速度范围[0,10]整数|
|turtle.circle()	|画圆,半径为正(负),表示圆心在画笔的左边(右边)画圆|

画笔控制命令

|命令|说明|
|:------:|:------:|
|turtle.pensize(width)	|绘制图形时的宽度|
|turtle.pencolor()	|画笔颜色|
|turtle.fillcolor(colorstring)	|绘制图形的填充颜色|
|turtle.color(color1, color2)	|同时设置pencolor=color1, fillcolor=color2|
|turtle.filling()	|返回当前是否在填充状态|
|turtle.begin_fill()	|准备开始填充图形|
|turtle.end_fill()	|填充完成|
|turtle.hideturtle()	|隐藏箭头显示；|
|turtle.showturtle()	|与hideturtle()函数对应|

全局控制命令

|命令|说明|
|:------:|:------:|
|turtle.clear()	|清空turtle窗口，但是turtle的位置和状态不会改变|
|turtle.reset()	|清空窗口，重置turtle状态为起始状态|
|turtle.undo()	|撤销上一个turtle动作|
|turtle.isvisible()	|返回当前turtle是否可见|
|stamp()	|复制当前图形|
|turtle.write(s[,font=("font-name",font_size,"font_type")])	|写文本，s为文本内容，font是字体的参数，里面分别为字体名称，大小和类型；font为可选项, font的参数也是可选项|

```python
# 绘制一个五角星
import turtle
import time

turtle.setup(1500, 1400, 0, 0)
turtle.pensize(5)
turtle.pencolor("pink")
turtle.fillcolor("red")

turtle.begin_fill()

for _ in range(5):
    turtle.forward(400)
    turtle.right(144)
turtle.end_fill()
time.sleep(5)
```