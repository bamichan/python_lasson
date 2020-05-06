"""
input()メソッドを使い、
Humanクラスを作成し、nameとbirthdayというインスタンス変数に名前と誕生日を入力してください。
クラスのインスタンスへの変数代入はコンストラクタを利用してください。

インスタンスへ変数代入後、最後に名前と誕生日を出力してください。
出力するときは、インスタンス変数を用いて出力させましょう

名前の入力は、ターミナル(コマンドプロンプト)から行ってください。
ターミナルから入力を行うにはinput()メソッドを使えばできます。

まずは、下記の例１になるように実装してみましょう。
-------------実行結果：例１
あなたについて教えて下さい
名前を入力してください：◯◯◯◯
誕生日を入力してください。例 2003/07/09：◯◯◯◯/◯◯/◯◯

名前は ◯◯◯◯
誕生日は ◯◯◯◯/◯◯/◯◯
-------------実行結果：例１ 以上

下記の、例２は余裕があれば挑戦してみてください。
・名前の入力のときに、空白を入力したら再度入力を求める。
・誕生日の入力のときに「◯◯◯◯/◯◯/◯◯」以外のフォーマットで入力すると再度入力を求める
-------------実行結果：例２
あなたについて教えて下さい
名前を入力してください：
１文字以上の入力が必要です。
名前を入力してください：SUNABACO
誕生日を入力してください。例 2003/07/09：2003/7/9
フォーマットが違います
誕生日を入力してください。例 2003/07/09：2003/07/09

名前は SUNABACO
誕生日は 2003年07月09日
-------------実行結果：例２ 以上
"""

from datetime import datetime
import re # 正規表現 実行結果例２を実装するときに使用します。
# ここに Human クラスを作成
class Human:
  def __init__(self,name,birthday):
    # コンストラクタ
    self.name = name
    self.birthday = self.__date_conversion(birthday)

  # インスタンスメソッドを定義
  def information(self):
    print('')
    print('名前は',self.name)
    print('誕生日は',self.birthday.strftime('%Y年%m月%d日'))
    print('')
  
  # プライベートメソッド
  # Pythonではメソッド名の前に __ をつけると、このクラス内でしかアクセスできないメソッドとなる。
  def __date_conversion(self, birthday):
    # inputの1111/11/11の文字列をdatetimeに
    return datetime.strptime(birthday, '%Y/%m/%d')

  # クラスメソッド、インスタンスを生成せずに直接呼び出すことが出来るメソッド
  @classmethod
  def input_name(cls):
    while True:
      your_name = input('名前を入力してください：')
      if your_name == '':
        print('１文字以上の入力が必要です。')
      else:
        break
    return your_name

  @classmethod
  def input_birthday(cls): # cls の中には Humanクラス が代入される
    while True:
      birthday = input('誕生日を入力してください。例 2003/07/09：')
      if cls.__check_birthday(birthday):
        break
      else:
        print('フォーマットが違います')
    return birthday

    @classmethod
    def __check_birthday(cls,birthday):
      """
      例外処理 '2019/11/11' 以外のフォーマットは False を返す。
      まずは tryのブロックが実行される
      re は正規表現を利用することができるクラス
      re.search()でマッチしなかったら None となり、 group()メソッドを実行するとエラー
      tryブロック内でエラーが発生すると、pythonの処理をとめずに、exceptブロックを実行する
      """
      try:
        return re.search(r'\d{4}\/d{2}\/|d{2}',birthday).group()
        # birthday変数の中に入っている文字列の中に数字4/数字2/数字2のような形式の文字が含まれるか検索
        # 含まれると re.Match というオブジェクトが戻り値となり、その戻り値に grouo()メソッド使うと実際に検索した文字列を戻り値として受け取る
        # 検索して該当する文字が含まれない場合は None が戻り値
      except:
        return False

print('あなたについて教えて下さい')
your_name = Human.input_name()
your_birthday = Human.input_birthday()

# Human クラスからインスタンス生成
you = Human(name=your_name, birthday=your_birthday)
# インスタンスメソッドinformation()を用いて情報を出力
you.information() 

"""
print('あなたについて教えて下さい')
while True:
  name = input('名前を入力してください：')
  if name == '':
    print('１文字以上の入力が必要です。')
  else:
    break
while True:
  birthday = input('誕生日を入力してください。例 2003/07/09：')
  if len(birthday) != 10:
    print('フォーマットが違います')
  else:
    break

print('名前は '+name)
print('誕生日は '+birthday)
"""