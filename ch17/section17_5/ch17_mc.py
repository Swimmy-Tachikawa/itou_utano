"""ch17_mc01.py
非同期処理を使ってMinecraftを制御します。
基準の位置からの距離によってブロックを置くタイミングを変え、10×10×10の立方体を作りましょう。
"""
import asyncio
from mcpi.minecraft import Minecraft
from preparation import prepare_site

mc = Minecraft.create()

pos = mc.player.getTilePos()

prepare_site(mc, 20, 20, 20)

mc.player.setTilePos(10, 10, 10)

DIAMOND_ID = 57
