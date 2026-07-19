"""ch2_pr03.py
変数last_nameには自分の苗字を、変数first_nameには自分の名前を代入し、
f-stringを使って"私の名前は〇〇〇〇です"という形式でフルネームを出力しましょう。
"""
# 変数last_nameに名字を代入する
last_name = "Ito"

# 変数first_nameに名前を代入する
first_name = "utano"

# f-stringを使って変数を埋め込んで出力する
print(f"{last_name  first_name}")
print(f"{last_name}　{first_name} 宛")

#print(last_name + first_name)