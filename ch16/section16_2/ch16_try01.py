"""ch16_try01.py
コードを実行して動作を確認してください。
"""

# 文字列の元のクラス（型）を確認
print(type("Hello"))

# print関数の元のクラス（型）を確認
print(type(print))


def greet():
    print("こんにちは")


# 関数の元のクラス（型）を確認
print(type(greet))


class Robot:
    def __init__(self, name):
        self.name = name


# インスタンスの元のクラス（型）を確認
robot = Robot("ロボ太")
print(type(robot))
