"""ch2_mc01.py
テキストのコードを打ち込んで実行してください。
"""
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# プレイヤーの位置情報を取得する
pos=mc.player.getTilePos()

# 石ブロックを置く
mc.setBlock(pos.x,pos.y,pos.z,1)