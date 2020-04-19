# -*- coding:utf-8 -*-

print("Guess Gameing")
temp = input("哪个数字呢？")
guess = int(temp)

if guess == 8:
    print("卧槽,你竟然才对了。")
    print("")
else:
    print("你猜错了，我的数字是8")
print("Game Over")
