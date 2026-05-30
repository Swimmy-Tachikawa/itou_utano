"""ch8_ex06.py
次のプログラムの出力は、A〜Dのどれになるでしょうか。
口頭で答えてみましょう。

A. [1, 2, 3, 4, 5]
B. [3, 4]
C. [1, 2]
D. [3, 4, 5]
"""
num = 0
arr = []

while num < 5:
    num = num + 1
    if num < 3:
        continue
    arr.append(num)

print(arr)
