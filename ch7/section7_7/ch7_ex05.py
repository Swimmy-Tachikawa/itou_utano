"""ch7_ex05.py
Minecraft上で、現在地を基準として、
大きな穴を掘る関数dig_hole()を作りましょう。

引数には穴のwidth（幅）、length（奥行き）、depth（深さ）の3つを指定できるようにしましょう。
範囲内のブロックを全て空気ブロックに置き換えることで穴を掘ることができます。
（空気ブロックのID：0）
"""
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
