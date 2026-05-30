"""ch8_ex09.py
次のプログラムの出力は、A〜Dのどれになるでしょうか。
口頭で答えてみましょう。

A. 勝ち
B. 負け
C. 出力なし
D. IndexError
"""
flag = False
array = [0, 1, 2]

for value in array:
    if value == 2:
        flag = True

if flag:
    print("勝ち")
else:
    print("負け")
