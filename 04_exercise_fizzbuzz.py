"""
1から100までの数字の中で
3の倍数の時は Fizz
5の倍数の時は Buzz
3の倍数かつ5の倍数の時は FizzBuzz と表示させてください！！ 
繰り返し文と条件文を使って下に書いてみてください。
"""
for i in range(1,101):
  if i%15==0:
    print('FizzBuzz')
  elif i%5==0:
    print('Buzz')
  elif i%3==0:
    print('Fizz')
  else:
    print(i)