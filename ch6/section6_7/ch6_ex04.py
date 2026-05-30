"""ch6_ex04.py
Minecraft上に、よこ5×奥行き2×高さ3となるTNTブロックのかたまりを作ってみましょう。
TNTブロックにはデータ値を指定して、爆発するようにしましょう。
（TNTブロックのID：46、データ値：1）
"""
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
