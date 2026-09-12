"""ch2_mc04.py
プレイヤーの今いる1つ下のブロック情報を出力して、そのブロックを木材ブロックに変えてみましょう。
その後、もう一度ブロック情報を出力してみましょう。
"""
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# プレイヤーの位置情報を取得し、変数posに代入する
pos=mc.player.getTilePos()

# プレイヤーの今いる1つ下のブロック情報を取得して表示する
block_id=mc.getBlock(pos.x,pos.y-1,pos.z)
print(block_id)

# mc.setBlock()を使って、1つ下を木材ブロックに変える
mc.setBlock(pos.x,pos.y-1,pos.z,5)

# プレイヤーの今いる1つ下のブロック情報を取得して表示する
block_id2=mc.getBlock(pos.x,pos.y-1,pos.z)
print(block_id2)