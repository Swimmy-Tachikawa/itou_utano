"""main.py
preparation.pyに定義されている関数を呼び出してみましょう。
"""
from mcpi.minecraft import Minecraft
from preparation import prepare_site

mc = Minecraft.create()

prepare_site(mc, 50, 50, 50, is_player_teleport=True)
