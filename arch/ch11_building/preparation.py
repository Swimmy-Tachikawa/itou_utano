from mcpi.minecraft import Minecraft

mc = Minecraft.create()


# 建築前の準備をする関数
def prepare_site(mc, x, y, z, is_player_teleport=True):
    """
    指定された範囲のブロックを空気ブロック（ID: 0）に置き換える関数

    引数:
        mc (Minecraft): Minecraftへの接続オブジェクト
        x, y, z (int): (-x, 0, -z)から(x, y, z)の範囲を整地する
        is_player_teleport (bool): プレイヤーを原点に移動させるかどうか
    """
    AIR_ID = 0
    WOOL_ID = 35
    RED_WOOL_DATA = 14
    BLUE_WOOL_DATA = 11
    WHITE_WOOL_DATA = 0

    # 範囲内のブロックをすべて空気ブロックに置き換える
    mc.setBlocks(-x, 0, -z, x, y, z, AIR_ID)

    # y = -1に草ブロックを配置する
    mc.setBlocks(-x, -1, -z, x, -1, z, 2)

    # x軸に赤色の羊毛ブロックを配置する
    mc.setBlocks(-x, -1, 0, x, -1, 0, WOOL_ID, RED_WOOL_DATA)

    # z軸に青色の羊毛ブロックを配置する
    mc.setBlocks(0, -1, -z, 0, -1, z, WOOL_ID, BLUE_WOOL_DATA)

    # 中心に白色の羊毛ブロックを配置する
    mc.setBlock(0, -1, 0, WOOL_ID, WHITE_WOOL_DATA)

    # プレイヤーを原点に移動させる
    if is_player_teleport:
        mc.player.setTilePos(0, 0, 0)


# このファイルが直接実行された場合にのみ実行
if __name__ == "__main__":
    prepare_site(mc, 32, 40, 41, is_player_teleport=True)
