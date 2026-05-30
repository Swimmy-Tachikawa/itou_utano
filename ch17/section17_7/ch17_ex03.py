"""ch17_ex03.py
動物たちが50m走をする以下のプログラムがあります。
現在は動物たちが順番にスタートしますが、プログラムを修正し、一斉にスタートして競争できるようにしてください。
Animalクラスの引数には動物名と時速を指定します。
"""

from time import sleep

class Animal:
    def __init__(self, name, kmh):
        self.name = name
        # 時速を秒速に変換
        self.mps = kmh * 1000 / 3600

    def race(animal, dist):
        print(f"{animal.name}がスタート！")
        # ゴールまでの時間を計算
        sleep(dist / animal.mps)
        print(f"{animal.name} がゴール！")

def main():
    cheetah = Animal("チーター", 110)
    horse = Animal("ウマ", 60)
    human = Animal("ヒト", 20)

    # 50mで競争
    cheetah.race(50)
    horse.race(50)
    human.race(50)

if __name__ == "__main__":
    main()
