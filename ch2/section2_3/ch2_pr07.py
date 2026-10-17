"""ch2_pr07.py
文字列"123"を数値に変換して、456と足し算をしてみましょう。
"""
# 変数textに"123"を代入する
text=str(123)


# textを数値に変換し、456と足し合わせて変数resultに代入する
text=int(text)
result = 456+text

# 結果を表示する
print(f"{result}")