"""
じゃんけんゲーム作成問題
以下に user_input という変数があります。これはターミナル(コマンドプロンプト)からの入力を受け取ることができます。
受け取った値をもとに勝ち、負けの判定をするじゃんけんゲームを作成してください

ただし、出力の言葉は以下を用いること
入力者が
勝ち -> 「あなたの勝ち」と出力
負け -> 「あなたの負け」と出力
あいこ -> 「引き分け」と出力

出力フォーマット例
---
あなた：グー
コンピュータ：パー
結果：あなたの負け
---

例１
【入力】
グー・チョキ・パー のいずれかを入力してください：グー

【出力】
あなた：グー
コンピュータ：パー
結果：あなたの負け


【補足】
ここでは、「import」というものを用いて pythonに標準機能である 「random」というモジュール（ライブラリ）を使用します。
リストの中のものをランダムに出力してくれる便利なモジュールです
"""

import random
user_input = input('グー・チョキ・パー のいずれかを入力してください：')

# 以下にコーディングしてください
com_choice = random.choice(['グー', 'チョキ', 'パー'])
results = ['あなたの勝ち', 'あなたの負け', '引き分け']
result = ''


if user_input == com_choice:
    result = results[2]
    # result = 'ひきわけ'

else:
    if user_input == 'グー':
        if com_choice == 'チョキ':
            result = results[0]
            # result = 'あなたの勝ち'
        else:
            result = results[1]
            # result = 'あなたの負け'

    elif user_input == 'チョキ':
        if com_choice == 'パー':
            result = results[0]
            # result = 'あなたの勝ち'
        else:
            result = results[1]
            # result = 'あなたの負け'

    elif user_input == 'パー':
        if com_choice == 'グー':
            result = results[0]
            # result = 'あなたの勝ち'
        else:
            result = results[1]
            # result = 'あなたの負け'


# いろんな print のしかたがあるよー
print('あなた：' + user_input)
print('コンピュータ：' + com_choice)
print('結果：' + result)
# printのしかた
print('---------------------------------')
# {}とformat(変数名)はセットで使う、ここでの{}は辞書型ではありません
print('あなた：{user_input2}'.format(user_input2=user_input))
# format()で指定した変数名をそのまま{}内のキーワード名に指定すると、{}内に指定したキーワード名と全く同じ名前の変数が埋め込まれます
print('コンピュータ：{com_choice}'.format(com_choice=com_choice))
print('結果：{result}'.format(result=result))

print('---------------------------------')

# print(f'あなた：{user_input}')
#      # f文字列（フォーマット文字列）の基本的な使い方
# print(f'コンピュータ：{com_choice}')   # f文字列（f-strings）は文字列の前にfまたはFを置く（f'xxx{変数名}', F'xxx{変数名}'）文字列中の置換フィールドに変数をそのまま指定できる。
# print(f'結果:{result}')

# format例↓
# ------------------------------------------------
# apple  = 50
# orange = 100
# total = apple + orange
# print(total)
# print('合計：{}円'.format(total))
# ------------------------------------------------

# ジャンケンで他の入力した時の例↓
# ------------------------------------------------
# elif user_input != com_choice:
#   user_input = '入力ミスだよ...'
#   com_choice = 'あんた間違ってる...'
#   result = '適切なじゃんけんをしてください'
# ------------------------------------------------

"""
# 参考: https://staku.designbits.jp/check-janken/

import random

score_lst = {'グー': 0, 'チョキ': 1, 'パー': 2}

user_input = input('グー・チョキ・パー のいずれかを入力してください：')
user_input_score = score_lst[user_input]

com_choice = random.choice(['グー', 'チョキ', 'パー'])
com_choice_score = score_lst[com_choice]

score = (user_input_score - com_choice_score + 3) % 3

print('あなた：' + user_input)
print('コンピュータ：' + com_choice)
print('結果：' + ['引き分け', 'あなたの負け', 'あなたの勝ち'][score])
print('---------------------------------')
"""

"""
#条件が長くなっている
hands=['グー','チョキ','パー']
print('あなた：'+user_input)
computer_hand=random.choice(hands)
print('コンピュータ：'+computer_hand)
if (user_input=='グー' and computer_hand=='チョキ') or (user_input=='チョキ' and computer_hand=='パー') or (user_input=='パー' and computer_hand=='グー'):
  print('あなたの勝ち')
elif (user_input=='グー' and computer_hand=='パー') or (user_input=='チョキ' and computer_hand=='グー') or (user_input=='パー' and computer_hand=='チョキ'):
  print('あなたの負け')
else:
  print('引き分け')
"""