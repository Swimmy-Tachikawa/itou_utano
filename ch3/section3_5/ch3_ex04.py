"""ch3_ex04.py
シェルからx座標、y座標、z座標のそれぞれの数値を入力させ、
入力された座標に瞬間移動するプログラムを作ってみましょう。
"""
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
x=int(input("x"))
y=int(input("y"))
z=int(input("z"))
mc.player.setTilePos(x,y,z)