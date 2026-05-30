"""ch15_ex01.py
次のプログラムを実行したときの出力はA〜Dのどれでしょうか。　　　
口頭で答えてみましょう。

A. 6
   引数が不適切です

B. 2
   引数が不適切です
   3

C. 2
   引数が不適切です

D. 6
   引数が不適切です
   3
"""


def output(arr):
    if (type(arr) is not list):
        raise Exception("引数が不適切です")
    print(len(arr))


japanese = [
    [1, 2, 3],
    ["一", "二", "三"],
]

try:
    output(japanese)
    output(japanese[0][1])
    output(japanese[0])
except Exception as e:
    print(e)
