"""ch2_ex05.py
ex4であけた穴に入り、自分の3ブロック上にトラップドアを設置しましょう。
（トラップドアのID：96、データ値：3）
"""
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
pos=mc.player.getTilePos()
mc.setBlock(pos.x,pos.y+3,pos.z,96,3)