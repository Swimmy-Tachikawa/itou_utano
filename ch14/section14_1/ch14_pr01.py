"""ch14_pr01.py
次のプログラムを実行すると、A〜Dのどの種類のエラーが出力されるでしょうか。口頭で答えてみましょう。

A. SyntaxError
B. ZeroDivisionError
C. NameError
D. TypeError
"""


def divide_numbers(a, b):
    return a / b

print(divide_num(0, "3"))
