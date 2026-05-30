"""ch15_ex07.py
二次元リストをMinecraft上の標高データとして扱います。
例えば3の要素は、その地点のy方向に3つのブロックが積み上げられていることを表します。

任意の標高データ（二次元リスト形式）を引数height_map、出力するブロックIDを引数block_idで受け取り、
それをMinecraft上に出力するgenerate_terrain関数を作りましょう。
オリジナルの標高データを作り、generate_terrainの引数に指定することで、面白い地形を作ってみましょう。
"""

from mcpi.minecraft import Minecraft

mc = Minecraft.create()
