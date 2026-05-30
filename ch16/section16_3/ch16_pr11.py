"""ch16_pr11.py
次のプログラムの出力はA〜Dのどれでしょうか。
口頭で答えてみましょう。

A. 私の名前はSwimmy太郎です。

B. 私はSwimmy学園に通っています。

C. 私の名前はSwimmy太郎です。
   私はSwimmy学園に通っています。

D. TypeError
"""

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"私の名前は{self.name}です。")


class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school

    def introduce(self):
        super().introduce()
        print(f"私は{self.school}に通っています。")


student = Student("Swimmy太郎", "Swimmy学園", "1年生")
student.introduce()
