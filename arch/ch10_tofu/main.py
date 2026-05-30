from mcpi.minecraft import Minecraft
from preparation import prepare_site

mc = Minecraft.create()

### 整地 ###

prepare_site(mc, 20, 20, 20)

### 豆腐建築 ###

"""定数の定義"""
OAK_PLANKS_ID = 5  # オークの木材ブロック
AIR_ID = 0  # 空気ブロック
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
GLASS_PANE_ID = 102  # ガラス板ブロック
STONE_BRICK_STAIRS_ID = 109  # 石レンガの階段ブロック
# 階段ブロックのデータ値
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
SLAB_ID = 44  # ハーフブロック
STONE_BRICK_SLAB_DATA = 5  # 石レンガのハーフブロックのデータ値


"""壁を作る"""


"""ドアを作る
オークの木材のドアのID・データ値:
    下の段→東向き: 64, 0
    上の段→左側に蝶番: 64, 9
"""


"""窓を作る"""


"""屋根を作る
石レンガの階段のID・データ値:
    屋根の左半分→南向き: 109, 2
    屋根の右半分→北向き: 109, 3
"""


"""自由課題
例: 床, えんとつ, 松明, ベッドや本棚などの内装
"""
