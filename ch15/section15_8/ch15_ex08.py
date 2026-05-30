"""ch15_ex08.py
generate_terrain関数をうまく使って、
50×50の範囲にそれぞれ1~10のランダムな高さのダイヤブロックを積み上げる、「水晶バイオーム」プログラムを作りましょう。
引数に指定する二次元リストはfor文で生成する必要があります。
"""

from mcpi.minecraft import Minecraft
import random

mc = Minecraft.create()
