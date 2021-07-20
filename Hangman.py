#Hangman
import os
choice=input('Want to play Hangman(y or n): ')
while choice=='y':
  #clear
  clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
  clear()
  #chance
  chance=5
  #variable
  import turtle
  screen=turtle.Screen()
  turtle.clearscreen()
  t=turtle
  m=turtle
  turtle.ht()
  #hang
  if chance==5:
    t.color('black')
    t.pensize(10)
    t.speed(2)
    t.pu()
    t.backward(100)
    t.pd()
    t.forward(50)
    t.pu()
    t.backward(100)
    t.pd()
    t.forward(50)
    t.left(90)
    t.forward(150)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(10)
    t.right(90)      
  #words
  if chance>0:
    def words():
      a=["india","america","africa","japan"]
      import random
      return(random.choice(a))
    word=words()
    word=list(word)
    #design
    print('Name of countries')
    print('\nYour word is..','_ '*len(word))
    result='-'*len(word)
    result=list(result)
    guess=input('\nEnter your choice: ')
    #loop1
    if guess in word:
      for i in range(len(word)):
        if word[i]==guess:
          result[i]=guess
          print("".join(result))
    else:
      chance=chance-1
      print('Wrong guess, try again\t\t\tChances left:',chance)
  #loop2
  while True:
    #man
    if guess not in word:
      if chance==4:
        m.color('red')
        m.pensize(5)
        m.speed(1)
        m.circle(20)
      if chance==3:
        m.left(90)
        m.pu()
        m.forward(40)
        m.pd()
        m.forward(30)
      if chance==2:
        m.left(30)
        m.forward(40)
        m.pu
        m.right(180)
      if chance==1:
        m.forward(40)
        m.pd
        m.left(120)
        m.forward(40)
    #result
    if guess in word:
      if result==word:
        print('\nIt\'s',''.join(word),'You Won!\n')
        break
    if chance>0:
      guess=input('Enter another choice: ')
      #another guess
      if guess in word:
        for i in range(len(word)):
          if word[i]==guess:
            result[i]=guess
            print("".join(result))
      else:
        chance=chance-1
        print('Wrong guess, try again\t\t\tChances left:',chance)
    if chance==0:
      m.left(180)
      m.pu

      m.forward(40)
      m.left(30)
      m.forward(15)
      m.pd
      m.right(90)
      m.forward(30)
      m.pu
      m.backward(30)
      m.pd
      m.backward(30)
      print('Wrong guess, Better luck next time\n')
      break
  choice=input('Want to play Hangman again(y or n): ')
else:
  exit