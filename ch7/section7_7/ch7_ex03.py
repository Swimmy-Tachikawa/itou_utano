"""ch7_ex03.py
次のプログラムを実行したときの出力はA〜Dのどれでしょうか。
口頭で答えてみましょう。

A.
りんごはapple
バナナはbanana

B.
出力なし

C.
りんごは200円
バナナは100円

D.
apple:200円
banana:100円
"""
sample_dict = {"apple": "200円", "banana": "100円"}

for fruit in sample_dict:
    match fruit:
        case "apple":
            print("りんごは" + sample_dict[fruit])
        case "banana":
            print("バナナは" + sample_dict[fruit])
