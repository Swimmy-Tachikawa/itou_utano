"""ch6_ex02.py
次のプログラムを実行したときの出力はA〜Dのどれでしょうか。口頭で答えてみましょう。

A. [1, 2, 3, 4]
B. [0, 1, 2, 3]
C. range(5)
D. [0, 1, 2, 3, 4]
"""
num_list = []

for i in range(5):
    num_list.append(i)

num_list.pop(0)

print(num_list)
