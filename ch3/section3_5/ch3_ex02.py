"""ch3_ex02.py
次のプログラムの出力は、A〜Dのどれになるでしょうか。口頭で答えてみましょう。

A. Hello!
B. greet("Taro")
C. Hello,Taro!
D. Hello Taro
"""


def greet(name):
    return "Hello," + name + "!"


print(greet("Taro"))
