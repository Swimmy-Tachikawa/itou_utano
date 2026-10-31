"""ch4_eg03.py
テキストのコードを打ち込んで実行してください。
"""
# 数字を入力させる
data=input("半角数字で数値を入力してください：")

# 数値に変換する
num=int(data)

# プラスの数字か、0か、マイナスの数字を判断する
if num>0:
    result="プラス"
elif num==0:
    result="ゼロ"
else:
    result="マイナス"
# 結果を表示する
print(result)