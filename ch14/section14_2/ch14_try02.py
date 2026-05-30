"""ch14_try02.py
コードを実行して動作を確認してください。
"""


# 入力された数字を表示
def display_number():
    num = int(input("数字を入力してください:"))
    print(f"入力された数字は{num}です")


# ずっとくり返す
while True:
    display_number()
