"""ch7_mc01.py
Minecraftの座標はタプルを使って表すことができます。
変数posに好きな座標の要素をもったタプルを代入し、その位置に瞬間移動してみましょう。
"""
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# 変数posに座標のタプルを代入する


# mc.player.setTilePos()の引数にposを指定し、瞬間移動する
