"""ch3_ex05.py
プレイヤーの位置情報を取得し、その位置にブロックを置く処理をまとめて、
関数「set_block_here」を作ってみましょう。
引数にはblock_idを用意し、指定したIDのブロックを置くようにしましょう。
"""
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
def set_block_id(block_id):
    pos=mc.player.getTilePos()
    mc.setBlock(pos.x,pos.y,pos.z,block_id,1
    )
set_block_id(46)