"""ch4_mc04.py
プレイヤーのいるy座標が20以上、かつ足元が空気ブロックのとき、
Minecraftのチャットに"Flying high!"と表示するプログラムを作ってみましょう。
（空気ブロックのID：0）
"""
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

