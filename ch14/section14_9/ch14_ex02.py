"""ch14_ex02.py
次のプログラムを実行したときの出力はA〜Dのどれでしょうか。
口頭で答えてみましょう。

A. 13は素数です
   入力に誤りがあります

B. 13は素数です
   入力に誤りがあります
   10は素数ではありません

C. 13は素数ではありません
   入力に誤りがあります
   10は素数ではありません

D. 13は素数ではありません
   入力に誤りがあります
"""


def checkPrimeNumber(num):
    divisorCount = 0

    if num < 0:
        raise Exception("入力に誤りがあります")
    for i in range(1, num + 1):
        if num % i == 0:
            divisorCount = divisorCount + 1
    if divisorCount == 2:
        print(str(num) + "は素数です")
    else:
        print(str(num) + "は素数ではありません")


try:
    checkPrimeNumber(13)
    checkPrimeNumber(-3)
    checkPrimeNumber(10)
except Exception as e:
    print(e)
