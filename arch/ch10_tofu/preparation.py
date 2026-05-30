from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()


# 建築前の準備をする関数
def prepare_site(mc, x, y, z):
    """
    指定された範囲のブロックを空気ブロック（ID: 0）に置き換える関数

    引数:
        mc (Minecraft): Minecraftへの接続オブジェクト
        x, y, z (int): (-x, 0, -z)から(x, y, z)の範囲を整地する
    """
    # 範囲内のブロックをすべて空気ブロックに置き換える
    AIR_ID = 0
    mc.setBlocks(-x, 0, -z, x, y, z, AIR_ID)

    # y = -1に草ブロックを配置する
    mc.setBlocks(-x, -1, -z, x, -1, z, 2)

    # x軸に赤色の羊毛ブロックを配置する
    WOOL_ID = 35
    WOOL_DATA = 14
    mc.setBlocks(-x, -1, 0, x, -1, 0, WOOL_ID, WOOL_DATA)

    # z軸に青色の羊毛ブロックを配置する
    WOOL_DATA = 11
    mc.setBlocks(0, -1, -z, 0, -1, z, WOOL_ID, WOOL_DATA)

    # 中心に白色の羊毛ブロックを配置する
    WOOL_DATA = 0
    mc.setBlock(0, -1, 0, WOOL_ID, WOOL_DATA)

    # プレイヤーを原点に移動させる
    mc.player.setTilePos(0, 0, 0)

    # 1秒間停止する
    sleep(1)
