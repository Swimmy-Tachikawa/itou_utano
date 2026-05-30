"""ch9_pr03.py
座標(0, 0, 0)から、(0, 0, 20)まで、
1つずつ間隔をあけながら木材ブロックを配置するプログラムを作成しましょう。
ただし、setBlock関数は1回しか使えません。必ずrange関数を使うようにしましょう。
（木材ブロックのID：5）
"""
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
