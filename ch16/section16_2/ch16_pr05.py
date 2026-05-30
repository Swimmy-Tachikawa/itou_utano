"""ch16_pr05.py
次のプログラムの出力はA〜Dのどれでしょうか。
口頭で答えてみましょう。

A. トムの出席番号は20です。
   アレックスの点数は100点です。

B. ValueError

C. アレックスの出席番号は100です。
   トムの点数は20点です。

D. アレックスの出席番号は7です。
   トムの点数は87点です。
"""

class Student:
    def __init__(self, name, id, score):
        self.name = name
        self.id = id
        self.score = score

    def show_id(self):
        print(f"{self.name}の出席番号は{self.id}です。")

    def show_score(self):
        print(f"{self.name}の点数は{self.score}点です。")


alex = Student("アレックス", 7, 100)
tom = Student("トム", 20, 87)

alex.show_id()
tom.show_score()
