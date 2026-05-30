"""ch16_ex04.py
ex3のプログラムにクラスを1つだけ追加し、Minecraft上でも三目並べゲームをあそべるようにしましょう。
"""

import mcpi.minecraft as minecraft
import mcpi.block as block
import time


# ブロックID
AIR_ID = 0 # 空気ブロック
WOOL_ID = 35  # 羊毛ブロック
SLAB_ID = 44 # 石のハーフブロック

# 羊毛ブロックのデータ値
WOOL_COLORS_DATA = {
    "WHITE": 0,  # 白
    "BLACK": 15,  # 黒
}
