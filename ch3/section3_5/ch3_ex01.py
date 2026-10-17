"""ch3_ex01.py
指定された半径（cm）の円の面積を求める関数「circle_area」を作ってみましょう。
引数には半径を意味するradiusを用意し、シェルから入力された値を渡しましょう。
円の面積を求める公式は、
円の面積 = 半径 × 半径 × 円周率
です。円周率は3.14で計算してください。
"""
def circle_area(radius):
    circle=radius*radius*3.14
    print(circle)

x=int(input())
circle_area(x)

