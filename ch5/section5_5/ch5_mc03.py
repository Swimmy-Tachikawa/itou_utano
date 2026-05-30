"""ch5_mc03.py
while文を使って、20歩進んだら、もとの場所に戻ってしまう
「出口のない世界」プログラムを作ってみましょう。1歩は1ブロックで考えましょう。

プログラムの流れ：
① 歩数、スタート地点の座標、前の座標、今の座標を代入する4つの変数を用意します。
② while文の中で、過去の座標と現在の座標を比べて、一致していなければ歩数を1増やします。
③ 歩数が20になったらwhile文を抜け出し、スタート地点に戻ります。
"""
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# 変数stepsに0を代入する


# 変数start_posにスタート地点の座標を代入する


# 変数prev_posにstart_posを代入する


# stepsが20未満ならずっとくり返す

    # 変数current_posに現在地の座標を代入する


    # もしprev_posとcurrent_posが一致していなければ

        # stepsを1だけ増やす


        # 現在地の情報を更新するために、prev_posにcurrent_posを代入する


        # チャットに移動歩数を表示する


# スタート地点に戻す


# チャットに"Welcome back!"と表示する
