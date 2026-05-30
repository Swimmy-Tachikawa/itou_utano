"""ch15_ex05.py
プレイヤーの周囲の地面のブロックIDを調査し、二次元リストの地図として返す、
generate_map関数を作って実行しましょう。
引数にはradius（調査半径）と、depth（調査する深さ）を指定します。
（pos.y−1の地面を調べたいときはdepthに1を指定する）
"""

from mcpi.minecraft import Minecraft

mc = Minecraft.create()
