import random

class Janken():
  def __init__(self):
    self.janken = ['グー', 'チョキ', 'パー']
    self.draw = 'DRAW!'
    self.win = 'WINNER!!'
    self.lose = 'LOSER...'


  def ja_try(self):
    user = input('グー or チョキ or パー : ')
    pc = random.choice(self.janken)

    if user == pc:
      judge = self.draw

    else:
      if user == 'グー':
        if pc == 'チョキ':
          judge = self.win
        else:
          judge = self.lose

      elif user == 'チョキ':
        if pc == 'パー':
          judge = self.win
        else:
          judge = self.lose

      else:
        if pc == 'グー':
          judge = self.win
        else:
          judge  = self.lose
          
    print('PCが選んだのは:', pc)
    print('勝敗は:', judge)
