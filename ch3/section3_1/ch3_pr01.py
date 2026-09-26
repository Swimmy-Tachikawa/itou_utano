"""ch3_pr01.py
四角形の面積を計算する関数を作り、テキストの長方形の面積を計算してみましょう。
公式は面積 = たて × 横 です。
"""
# 関数「rectangle_area」を定義する。引数にはheight（たて）とwidth（よこ）を用意する。
def rectangle_area(height,weight):
# 変数ansに計算結果を代入する
    ans=height*weight

# returnを使ってansを返す
    return ans

# rectangle_areaを実行し、変数resultで戻り値を受け取る。関数の引数には2と4を指定する。
result=rectangle_area(4,2)

# print関数を使ってresultを出力する
print(result)