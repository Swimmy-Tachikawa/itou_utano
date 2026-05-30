"""ch3_mc04.py
jump関数をアレンジし、jump_and_land関数を作ってみましょう。
プレイヤーはpower分だけ上空に瞬間移動したあと、真下に石ブロックを置いてそこに着地します。
"""
from mcpi.minecraft import Minecraft

mc = Minecraft.create()


# 関数「jump_and_land」を定義する。引数にpowerを用意する。

    # mc.player.getTilePos()を使ってプレイヤーの位置情報を取得し、変数pos に代入する


    # mc.player.setTilePos()を使ってプレイヤーの位置を変更する。y座標を +power すると、power分だけ上に移動する。


    # mc.setBlock()を使って、移動した位置の真下に石ブロックを置く



# 引数を指定してjump_and_land関数を実行する

