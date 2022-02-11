import dataBase

import os
import sys
import time
import dataTemp
import random

def border(a):
  for i in range(a):
    print('─', end = '')
  else:
    print('')

def title(a, b):
  border(b)
  print(a.center(b))
  border(b)

def notif(a, b, c):
  print('')

  txt = '» '
  txt = txt + a
  txt = txt + ' «'

  print(txt.center(b))

  time.sleep(c)

def clear(a):
  if a == 'all':
    os.system('cls')
  else:
    for i in range(a):
      sys.stdout.write('\033[F')
      for j in range(50):
        print(' ', end = '')
      else:
        print(end = '\r')

def wait(a):
  time.sleep(a)
  
def loading(a, b):
  print('')

  for i in range(b+1):  
    txt = '  » ' + a + '.' * i
    print (txt, end = '\r')
    time.sleep(1)

  os.system('cls')

def giveCard(a, c, v):
  for i in range(a):
    c.append(dataTemp.deck.pop(0))
    key = c[-1]
    v.append(dataTemp.valueDeck[key])

def printFirstCard(a):
  print('[', a[0], ']', ' [?]', sep = '')
  print('     Total         : ?')
  print('')

def printCard(a):
  for i in range(len(a)):
    print('[', a[i], ']', sep = '', end = ' ')
  print('')

def printMenu():
  print('      ┌─────────┐      ┌─────────┐      ')
  print('      │   HIT   │      │  STAND  │      ')
  print('      └─────────┘      └─────────┘      ')

def printAll():
  print(' [»] Dealer\'s hand : ', end = '')
  printCard(dataTemp.dCard)
  print('     Total         : ', dataTemp.dTotal)
  
  print('')

  print(' [»] Your hand     : ', end = '')
  printCard(dataTemp.pCard)
  print('     Total         : ', dataTemp.pTotal)

def calculate():
  total = 0

  for i in dataTemp.pValue:
    total = total + i

  dataTemp.pTotal = total

  total = 0

  for i in dataTemp.dValue:
    total = total + i
    
  dataTemp.dTotal = total

  count = -1

  if 11 in dataTemp.pValue and dataTemp.pTotal > 21:
    for i in dataTemp.pValue:
      count += 1
      if i == 11:
        dataTemp.pValue.pop(count)
        dataTemp.pValue.insert(count, 1)
    calculate()
  
  if 11 in dataTemp.dValue and dataTemp.dTotal > 21:
    for i in dataTemp.dValue:
      count += 1
      if i == 11:
        dataTemp.dValue.pop(count)
        dataTemp.dValue.insert(count, 1)
    calculate()

def result(a):
  earn = dataTemp.bet + (dataTemp.bet * 0.65)
  a = a.upper()
  if a == 'TIE':
    wait(1)
    notif('TIE !', 50, 1)
    notif('You stood with same score with the dealer', 50, 1)
    notif('Your chip has been returned', 50, 1)

    dataBase.setChip(dataTemp.account, dataTemp.bet)
    dataBase.addLose(dataTemp.account)

    print('')
  elif a == 'BLACKJACK':
    wait(1)
    notif('YOU WIN !', 50, 1)
    notif('\"BLACK JACK\" You got to 21', 50, 1)
    notif('You earned ' + str(int(earn)) + ' chip', 50, 1)

    dataBase.setChip(dataTemp.account, earn)
    dataBase.addWin(dataTemp.account)

    print('')
  elif a == 'PBUSTED':
    wait(1)
    notif('YOU LOST !', 50, 1)
    notif('You went over 21 and busted', 50, 1)
    notif('You lost your chip', 50, 1)
    
    dataBase.addLose(dataTemp.account)

    print('')
  elif a == 'DBUSTED':
    wait(1)
    notif('YOU WIN !', 50, 1)
    notif('The dealer went over 21 and busted', 50, 1)
    notif('You earned ' + str(int(earn)) + ' chip', 50, 1)

    dataBase.setChip(dataTemp.account, earn)
    dataBase.addWin(dataTemp.account)
    
    print('')
  elif a == 'WIN':
    wait(1)
    notif('YOU WIN !', 50, 1)
    notif('You stood with a higher score than the dealer', 50, 1)
    notif('You earned ' + str(int(earn)) + ' chip', 50, 1)

    dataBase.setChip(dataTemp.account, earn)
    dataBase.addWin(dataTemp.account)

    print('')
  elif a == 'LOSE':
    wait(1)
    notif('YOU LOSE !', 50, 1)
    notif('You stood with a lower score than the dealer', 50, 1)
    notif('You lost your chip', 50, 1)
    
    dataBase.addLose(dataTemp.account)
    
    print('')

def reset():
  dataTemp.deck = list(dataTemp.baseDeck)
  for i in range(10):
    random.shuffle(dataTemp.deck)
  dataTemp.pCard.clear()
  dataTemp.pValue.clear()
  dataTemp.dCard.clear()
  dataTemp.dValue.clear()
  dataTemp.dTotal = 0
  dataTemp.pTotal = 0
  dataTemp.pCond = True
