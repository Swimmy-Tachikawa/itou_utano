from mcpi.minecraft import Minecraft
from preparation import prepare_site

mc = Minecraft.create()

### 整地 ###

prepare_site(mc, 26, 41, 36, is_player_teleport=True)

### 洋風建築 ###

import functions

"""壁を作る
松明のID・データ値:
    正面 (手順7) / front_wall_part(): 50, 2
    右向き (手順15) / right_wall_part(): 50, 3
    後ろ向き (手順15) / behind_wall_part(): 50, 1
    左向き (手順15) / left_wall_part(): 50, 4
"""
# 壁に使用する定数
STONE_ID = 1  # 石ブロック
QUARTZ_ID = 155  # ネザー水晶ブロック
SLAB_ID = 44  # ハーフブロック
STONE_SLAB_DATA = 0  # 石のハーフブロックのデータ値
AIR_ID = 0  # 空気ブロック
GLASS_PANE_ID = 102  # ガラス板ブロック
TORCH_ID = 50  # 松明ブロック
# 松明ブロックのデータ値
TORCH_DATA = {
    "UNDER": 0,  # 下側のブロックに設置
    "WEST": 1,  # 西側のブロックに設置
    "EAST": 2,  # 東側のブロックに設置
    "NORTH": 3,  # 北側のブロックに設置
    "SOUTH": 4,  # 南側のブロックに設置
}
OAK_FENCE_ID = 85  # オークの木のフェンスブロック


"""エントランスを作る
オークの木材のドアのID・データ値 / front_entrance_part():
    下半分 (手順4): 64, 0
    上半分 (手順4): 64, 9

ネザー水晶の階段のID・データ値 / entrance_roof():
    手順18: 156, 2
    手順19: 156, 6
    手順20: 156, 0
    手順21: 156, 4
    手順22: 156, 3
    手順23: 156, 7
"""
# エントランスに使用する定数
QUARTZ_STAIRS_ID = 156  # ネザー水晶の階段ブロック
STAIRS_DATA = {
    "EAST": 0,  # 東向き
    "WEST": 1,  # 西向き
    "SOUTH": 2,  # 南向き
    "NORTH": 3,  # 北向き
    "INVERTED_EAST": 4,  # 東向き（逆さま）
    "INVERTED_WEST": 5,  # 西向き（逆さま）
    "INVERTED_SOUTH": 6,  # 南向き（逆さま）
    "INVERTED_NORTH": 7,  # 北向き（逆さま）
}
OAK_DOOR_ID = 64  # オークの木材のドアブロック
# ドアブロックのデータ値
DOOR_DATA = {
    "BOTTOM_EAST": 0,  # 東向き（下半分）
    "BOTTOM_SOUTH": 1,  # 南向き（下半分）
    "BOTTOM_WEST": 2,  # 西向き（下半分）
    "BOTTOM_NORTH": 3,  # 北向き（下半分）
    "TOP_RIGHT": 8,  # 右側に蝶番（上半分）
    "TOP_LEFT": 9,  # 左側に蝶番（上半分）
}


"""屋根を作る
ネザーレンガの階段のID・データ値:
    front_roof()
        正面最下段 (手順1): 114, 4
        正面 (手順2-8): 114, 0

    behind_roof()
        後ろ向き最下段 (手順13): 114, 5
        後ろ向き (手順13): 114, 1

    left_roof()
        左向き最下段 (手順13): 114, 6
        左向き (手順13): 114, 2

    right_roof()
        右向き最下段 (手順13): 114, 7
        右向き (手順13): 114, 3
"""
# 屋根に使用する定数
NETHER_BRICK_STAIRS_ID = 114  # ネザーレンガの階段ブロック
NETHER_BRICK_ID = 112  # ネザーレンガブロック


"""自由課題
例: 床, 階段, 花壇, ベッドや本棚などの内装
"""
