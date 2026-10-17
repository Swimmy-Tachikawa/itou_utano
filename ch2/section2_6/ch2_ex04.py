"""ch2_ex04.py
プレイヤーの真下に3ブロック分の穴をあけてみましょう。
ブロックを空気ブロックに変換すると穴をあけることができます。
（空気ブロックのID：0）
"""
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

pos=mc.player.getTilePos()
mc.setBlock(pos.x,pos.y-1,pos.z,0)
mc.setBlock(pos.x,pos.y-2,pos.z,0)
mc.setBlock(pos.x,pos.y-3,pos.z,0)            