
# -*- coding:utf-8 -*-

# 函数作为返回值

# 实现一个可变参数的求和
def calc_sum(*args) :
    ax = 0
    for n in args :
        ax = ax + n
    return ax

# 但是,如果不需要立刻求和,而是在后面的代码中,根据需要再计算怎么办?可以不返回求和的结果,而是返回求和的函数:
def lazy_sum(*args) :
    def sum() :
        ax = 0
        for n in args :
            ax = ax + n
        return ax
    return sum

# 当我们调研lazy_sum()时,返回的并不是求和结果,而是求和函数
f = lazy_sum(1,3,5,7,9)
f # <funciton lazy_sum.<locals>.sum at 0x101c6ed90>
# 调研函数f时,才真正计算求和的结果:
f() # 25

"""
在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。

请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
"""
f1 = lazy_sum(1,3,5,7,9)
f2 = lazy_sum(1,3,5,7,9)
f1 == f2 # False
# f1()和f2()的调研结果互不影响

# 闭包
'''
注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。

另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。我们来看一个例子：
'''
def count() :
    fs = []
    for i in range(4) :
        def f() :
            return i*i
        fs.append(f)
    return fs
f1,f2,f3 = count()
# 在上面的例子中,每次循环,都创建了一个新的函数,然后,把创建的3个函数都返回了。
# 你可能认为调研f1(),f2()和f3()结果应该是1,4,9,但实际结果是:
f1() # 9
f2() # 9
f3() # 9