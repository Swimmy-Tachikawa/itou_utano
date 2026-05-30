"""ch6_ex05.py
羊毛ブロックは16色あり、0〜15のデータ値で指定することができます。
0〜15から好きな数字を5つ選び、color_listにリストオブジェクトとして代入しましょう。
その後、color_listの要素をデータ値として、5色の羊毛ブロックをx方向に一列に並べてみましょう。
（羊毛ブロックのID：35、データ値：0〜15）
"""
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

