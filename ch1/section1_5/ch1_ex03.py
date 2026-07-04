"""ch1_ex03.py
1分は60秒です。では、1日（24時間）は何秒でしょうか。
プログラムで計算し、表示してみましょう。
また、今日が終わるまでの残り時間を計算し、表示しましょう。
"""
# 変数minuteに1分の秒数を代入する
minute=60

# 変数hourに、minuteを使って1時間の秒数を代入する
hour=60*60

# 変数dayに、hourを使って1日の秒数を代入する
day=24*hour

# print関数を使ってdayを表示する
print(day)

# 変数current_timeに現在の秒数を計算して代入する
current_time=hour*10+minute*59

# 変数remaining_secondsに、dayとcurrent_timeを使って、今日が終わるまでの残り秒数を計算して代入する


# print関数を使ってremaining_secondsを表示する
