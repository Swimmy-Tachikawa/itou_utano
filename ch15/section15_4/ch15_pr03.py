"""ch15_pr03.py
次のプログラムを実行したときの出力はA〜Dのどれでしょうか。
口頭で答えてみましょう。

A. ["A", "B", "C", "D", "E"]
B. ["E", "D", "C", "B", "A"]
C. ['A', 'C', 'D', 'B', 'E']
D. ['E', 'B', 'D', 'C', 'A']
"""

arr = ["A", "C", "D", "B", "E"]

arr.sort(reverse=True)
arr.reverse()
print(arr)
