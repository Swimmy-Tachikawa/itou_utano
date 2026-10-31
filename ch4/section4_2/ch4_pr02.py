"""ch4_pr02.py
顔文字を3つ作ってそれぞれ変数に代入し、数字を入力させます。
入力された数字が10以下の場合は1つ目の顔文字を、
10より大きく20以下の場合は2つ目の顔文字を、
20より大きい場合は3つ目の顔文字を表示するプログラムを作りましょう。
"""
# face1、face2、face3にそれぞれ顔文字を代入する
face1=">u<"
face2="^v^"
face3="0x0"

# 変数numに、シェルから入力した数字を整数型に変換したオブジェクトを代入する
num=int(input("数字を入力してください："))

# もし、numが10以下なら
if num<=10:
    # 変数resultにface1を代入する
    result=face1
# でなければもし、numが20以下なら
elif num<=20:
    # 変数resultにface2を代入する
    result=face2
# でなければ
else :
    # 変数resultにface3を代入する
    result=face3

# 変数resultを出力する
print(result)