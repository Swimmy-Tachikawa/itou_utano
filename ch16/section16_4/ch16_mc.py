"""ch16_mc.py
クラスを使ってMinecraftの世界にロボットを作り、動かしてみましょう。
"""

from mcpi.minecraft import Minecraft

mc = Minecraft.create()

AIR_ID = 0  # 空気ブロック
WOOL_ID = 35  # 羊毛ブロック
# 羊毛ブロックのデータ値
WOOL_COLORS_DATA = {
    "WHITE": 0,  # 白
    "ORANGE": 1,  # 橙
    "MAGENTA": 2,  # マゼンタ
    "LIGHT_BLUE": 3,  # ライトブルー
    "YELLOW": 4,  # 黄色
    "LIME": 5,  # ライム
    "PINK": 6,  # ピンク
    "GRAY": 7,  # グレー
    "SILVER": 8,  # シルバー
    "CYAN": 9,  # シアン
    "PURPLE": 10,  # 紫
    "BLUE": 11,  # 青
    "BROWN": 12,  # 茶色
    "GREEN": 13,  # 緑
    "RED": 14,  # 赤
    "BLACK": 15,  # 黒
}
STONE_BRICK_ID = 98  # 石レンガのブロック
SLAB_ID = 44  # ハーフブロック
STONE_BRICK_SLAB_DATA = 13  # 石レンガのハーフブロック
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
