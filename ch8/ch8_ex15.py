"""ch8_ex15.py
ドアに入るとランダムな座標に瞬間移動してしまう、「どこでもドア」を作りましょう。
ドアは現在位置の目の前に設置し、瞬間移動する範囲はx, y, z全て1〜100にしましょう。
（扉ブロックのID：64）
"""
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

from random import randint
