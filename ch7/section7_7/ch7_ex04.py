"""ch7_ex04.py
Minecraft上で、東西南北すべての方向に両開き扉を設置する関数を作りましょう。

① create_east_door() # 東側
② create_west_door() # 西側
③ create_south_door() # 南側
④ create_north_door() # 北側

の関数をそれぞれ作り、実行するとプレイヤーが両開き扉に囲まれます。
テキストの図も参考にしてみてください。
（扉ブロックのID：64）
"""
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
