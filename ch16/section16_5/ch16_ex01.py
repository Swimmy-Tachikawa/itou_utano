"""ch16_ex01.py
次のプログラムの出力はA〜Dのどれでしょうか。
口頭で答えてみましょう。

A. カルボナーラは800円です

B. カルボナーラは900円です

C. カルボナーラは850円です

D. カルボナーラは700円です
"""

class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_info(self):
        print(f"{self.name}は{self.price}円です")

class Pasta(Food):
    def add(self, extra):
        self.price = self.price + extra


extra_menu = {
    "large": 100,
    "cheese": 50,
}

pasta = Pasta("カルボナーラ", 800)
pasta.add(extra_menu["large"])
pasta.show_info()
