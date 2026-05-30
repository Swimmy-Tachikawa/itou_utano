"""ch8_ex13.py
よこ（x）3×奥行き（z）3×高さ（y）3となる羊毛ブロックのかたまりを配置しましょう。
ブロック1つずつに0〜15のデータ値をランダムに指定して、カラフルになるようにしましょう。
ただし、setBlock関数は1回しか使えません。
(羊毛ブロックの ID：35、データ値：0 〜 15)
"""
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
