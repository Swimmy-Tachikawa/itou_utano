"""ch16_eg10.py
テキストのコードを打ち込んで実行してください。
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name}は動きました")

    # cryメソッド



# Catクラス
class Cat(Animal):
    def scratch(self):
        print(f"{self.name}は爪をとぎました")

    # cryメソッドをオーバーライド



# インスタンス化
cat = Cat("みけねこ")
cat.cry()
