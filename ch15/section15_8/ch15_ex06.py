"""ch15_ex06.py
プレイヤーから半径50ブロック内のどこかの地面（pos.y−2）に
ダイヤモンドブロック（ID：57）を埋めるプログラムを作りましょう。
その後、generate_map関数を使って地図を作り、ダイヤモンドを掘り当ててみましょう。
"""

from mcpi.minecraft import Minecraft
import random

mc = Minecraft.create()
