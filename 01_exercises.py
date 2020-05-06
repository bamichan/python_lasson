"""
Tips!
この "(ダブルクォーテーション)を3つを上下で囲ったものは
Pythonでは複数行のコメントアウトを記述するときに利用します。
参考 https://uxmilk.jp/8847
"""


"""
お題1: 今日の曜日は？
お題: 今日の曜日を日本語で表示させてください

import datetime
today = datetime.date.today()

today.day
をすると今日の日付が返ってきます。

today.weekday()
をすると曜日の数字が返って来ます。0が月曜日で、6が日曜日帰って来ます。
"""
import datetime
today = datetime.date.today()
today.day  # これは今日の日付
today.weekday()  # これは曜日の数字を取得

print("_________________________________")

# ここから下に解答を書く
# print("今日は木曜日です")
print(today.day)
print(today.weekday())

youbi = ("月", "火", "水", "木", "金", "土", "日")
# 変数youbiにタプル型("月","火","水","木","金","土","日")を代入

print("今日は" + youbi[today.weekday()] + "曜日です。")
# youbiの中身を[today.weekday()]を使って取り出す。

"""
# 非推奨
if today.weekday() == 0:
    week = '月'
elif today.weekday() == 1:
    week = '火'
elif today.weekday() == 2:
    week = '水'
elif today.weekday() == 3:
    week = '木'
elif today.weekday() == 4:
    week = '金'
elif today.weekday() == 5:
    week = '土'
else:
    week = '日'
print('今日は'+week+'曜日です')
"""
# 出力例 今日は水曜日です


#######################################################
print("_________________________________")


"""
お題2: 一番大きい数、小さい数字、平均値は？
お題: 配列の中の一番大きい数字、小さい数字、平均値をそれぞれ表示してください。
"""

numbers = [73, 24, 64, 10, 56, 89]


# ここから下に解答を書く
print(max(numbers))
print(min(numbers))
print(sum(numbers)/len(numbers))

"""
出力例
89
10
52.666666666666664
"""

#######################################################
print("_________________________________")


"""
お題3: 連絡先をを表示して
お題: dictに入ったデータを使って連絡先を整形して出力してみましょう。
"""

person = {
    "first_name": "太郎",
    "last_name": "すなば",
    "address": {
        "post_code": '904-0004',
        "prefecture": "沖縄県",
        "city": "沖縄市",
        "street": "中央1丁目14-3"},
    "phone": "080-1234-5678",
}

# ここから下に解答を書く
print('名前: '+person['last_name']+person['first_name'])
print('郵便番号: '+person['address']['post_code'])
print('住所: '+person['address']['prefecture'] +person['address']['city']+person['address']['street'])
print('電話番号: '+person['phone'])

"""
出力例
名前: すなば 太郎
郵便番号: 904-0004
住所: 沖縄県沖縄市中央1丁目14−3
電話番号番号: 080-1234-5678
"""

print("_________________________________")
