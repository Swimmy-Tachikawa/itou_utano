"""ch9_pr01.py
Minecraftの世界でプレイヤーの目の前（x + 1）に、
テキストの図と同じ形となるようにブロックを配置してみましょう。
ただし、setBlock関数は1回しか使えません。
（木材ブロックのID：5）
"""
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
