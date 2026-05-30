"""ch8_ex20.py
Minecraftのx-y平面に、現在位置を基準として
「○」の形に羊毛ブロックを配置する関数、
「×」の形に羊毛ブロックを配置する関数をそれぞれ作り、実行しましょう。
「○」は赤い羊毛ブロック、「×」は青い羊毛ブロックにしましょう。
（羊毛ブロックのID：35、赤色のデータ値：14、青色のデータ値：11）
"""
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
