"""ch2_ex02.py
次のプログラムの中で、①〜③のオブジェクトはint型、float型、str型のどれでしょうか。口頭で答えてみましょう。
input関数には何かの戻り値があるものとします。
① result1　　② result2　　③ result3
"""
result1 = 10 / 2 # ① int? -> float!
result2 = input() # ② str? -> str!
result3 = "1" + "1" # ③ str? -> str!

print(f"① {result1}", type(result1))
print(f"② {result2}", type(result2))
print(f"③ {result3}", type(result3))
