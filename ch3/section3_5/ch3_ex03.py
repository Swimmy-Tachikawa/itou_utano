"""ch3_ex03.py
みんなで動物園に行ったときの入園料を計算する関数「entry_fee」を作ってみましょう。
引数には大人の人数「adults」と、子どもの人数「children」を用意し、合計の入園料が計算されるようにします。
入園料は大人1人630円、子ども1人315円とします。
"""


# 関数entry_feeを定義する
def entry_fee(adult,children):
    # 大人と子どもの合計金額を計算し、戻り値として返す
    adultsum=adult*630
    childrensum=children*315
    return adultsum+childrensum
     
# シェルから大人の人数と子どもの人数を入力させ
adult=int(input("adult"))
children=int(input("children"))
# 関数entry_feeを呼び出して出力する。引数には入力された人数を指定する。
print("合計金額",entry_fee(adult,children))
