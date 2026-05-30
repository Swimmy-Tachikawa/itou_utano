"""ch9_pr02.py
座標(0, 0, 0)、(0, 0, 8)、(0, 0, 12)、 (0, 0, 20)
の4箇所に木材ブロックを配置するプログラムを作成しましょう。
ただし、setBlock関数は1回しか使えません。リストをうまく使ってz座標を指定しましょう。
（木材ブロックのID：5）
"""
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
