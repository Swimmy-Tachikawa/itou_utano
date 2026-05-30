"""ch14_pr04.py
次のプログラムの出力はA〜Dのどれになるでしょうか。
口頭で答えてみましょう。

A. 時速は 0 km/h です

B. Traceback (most recent call last):
    File "ch14_pr04.py", line 7, in <module>
    speed = calculate_speed(10, 0)
        ^^^^^^^^^^^^^^^^^^^^^^
    File "ch14_pr04.py", line 3, in calculate_speed
    raise ValueError("時間は0より大きい値を入力してください。")
    ValueError: 時間は0より大きい値を入力してください。

C. 時間は0より大きい値を入力してください。

D. SyntaxError
"""


def calculate_speed(distance, time):
    if time <= 0:
        raise ValueError("時間は0より大きい値を入力してください。")
    return distance / time


try:
    speed = calculate_speed(10, 0)
    print(f"時速は {speed} km/h です")
except ValueError as e:
    print(e)
