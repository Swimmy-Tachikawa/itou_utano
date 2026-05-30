from mcpi.minecraft import Minecraft
from preparation import prepare_site

mc = Minecraft.create()

### 整地 ###

prepare_site(mc, 25, 41, 25, is_player_teleport=True)

### 高層ビル ###

"""定数の定義"""
GLASS_ID = 20  # ガラスブロック
AIR_ID = 0  # 空気ブロック
QUARTZ_ID = 155  # ネザー水晶ブロック
QUARTZ_PILLAR_DATA = 2  # 柱状ネザー水晶ブロックのデータ値
WOOL_ID = 35  # 羊毛ブロック
GRAY_WOOL_DATA = 7  # 灰色の羊毛ブロックのデータ値
STONE_ID = 1  # 石ブロック
STONE_BRICK_STAIRS_ID = 109  # 石レンガの階段ブロック

"""壁を作る"""


"""床・天井を作る"""


"""エントランスを作る"""


"""自由課題
例: 階段, 屋上, 壁や床のアレンジ
"""
