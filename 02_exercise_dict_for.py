"""
exercises 課題3 を解き終えている前提です。
前回の課題３で使用したdictオブジェクトがリストオブジェクトの中に４つはいっています。
これをfor文を用いて出力してください。

for文例
book_lst = ['欲しい ほしい、ホシイ', '人工知能は人間を超えるか', 'BUSINESS FOR PUNKS']
for book in book_lst:
    print(book)

-----for文出力例
欲しい ほしい、ホシイ
人工知能は人間を超えるか
BUSINESS FOR PUNKS
-----for文出力例以上

"""

person_lst = [
    {
        "first_name": "コザ",
        "last_name": "スナバコ",      
        "address": {
            "post_code": "904-0004",
            "prefecture": "沖縄県",
            "city": "沖縄市",
            "street": "中央１丁目14−3"},
        "phone": "080-1111-1111",
    },
    {
        "first_name": "江別",
        "last_name": "スナバコ",      
        "address": {
            "post_code": "069-0852",
            "prefecture": "北海道",
            "city": "江別市",
            "street": "大麻東町13-6"},
        "phone": "080-1111-1111",
    },
    {
        "first_name": "いどば",
        "last_name": "スナバコ",      
        "address": {
            "post_code": "103-0012",
            "prefecture": "東京都",
            "city": "中央区日本橋",
            "street": "堀留町1丁目5-7 YOUビル8F"},
        "phone": "080-3963-3355",
    },
    {
        "first_name": "たかまつ",
        "last_name": "スナバコ",      
        "address": {
            "post_code": "760-0054",
            "prefecture": "香川県",
            "city": "高松市",
            "street": "常磐町1丁目3-1 瓦町FLAG 10F"},
        "phone": "080-1111-1111",
    }
]

# ここにfor文を書く
for person in person_lst:
    print("名前：" + person["last_name"] + person["first_name"])
    print("郵便番号：" + person["address"]["post_code"])
    print("住所：" +person["address"]["prefecture"] + person["address"]["city"] + person["address"]["street"])
    print("電話番号：" + person["phone"])
    print("")

for i in range(len(person_lst)):
    print('名前: '+person_lst[i]['last_name']+person_lst[i]['first_name'])
    print('郵便番号: '+person_lst[i]['address']['post_code'])
    print('住所: '+person_lst[i]['address']['prefecture'] +person_lst[i]['address']['city']+person_lst[i]['address']['street'])
    print('電話番号: '+person_lst[i]['phone'])