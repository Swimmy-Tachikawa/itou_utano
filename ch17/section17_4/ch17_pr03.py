"""ch17_pr03.py
次のようにCookクラスが定義されています。
インスタンス変数には料理名（menu）、秒数（seconds）を持ち、
moveメソッドが呼び出されたとき、秒数（seconds）だけ待って料理が完成します。
現在は3つの調理が順番に進むため、全ての料理が完成するのに約6秒かかります。
交互に調理が進むようプログラムを修正し、約3秒で全てが完成するようにしてください。
"""

from time import sleep

class Cook:
    def __init__(self, menu, seconds):
        self.menu = menu
        self.seconds = seconds

    def make(self):
        print(f"{self.menu} の調理開始！")
        sleep(self.seconds)
        print(f"{self.menu} が完成しました！")

def main():
    c1 = Cook("カレー", 3)
    c2 = Cook("サラダ", 1)
    c3 = Cook("スープ", 2)

    c1.make()
    c2.make()
    c3.make()

if __name__ == "__main__":
    main()
