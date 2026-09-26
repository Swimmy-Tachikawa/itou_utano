"""ch3_mc01.py
テキストのコードを打ち込んで実行してください。
"""
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# プレーヤーの位置情報を取得する
pos=mc.player.getTilePos()

# プレーヤーの位置情報を変更する
mc.player.setTilePos(pos.x-30,pos.y,pos.z)