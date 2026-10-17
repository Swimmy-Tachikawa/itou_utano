"""ch2_mc03.py
テキストのコードを打ち込んで、実行してみましょう。
"""
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# プレーヤーの位置情報を取得する
pos=mc.player.getTilePos()

# プレーヤーの今いる1つ下のブロック情報を取得する
block_id=mc.getBlock(pos.x,pos.y-1,pos.z)

# ブロックIDを表示する
print(block_id)