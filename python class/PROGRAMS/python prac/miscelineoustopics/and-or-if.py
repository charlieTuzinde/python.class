
score = eval(input('Enter your score: '))
if score>=25 and score<50:
   print('Your grade is a D.')
if score>=50 and score<80:
   print('Your grade is a B.')
if score>=80 and score<90:
   print('Your grade is a A.')
if score>1000 :
   print('Game over.')
if not (score>1000 ):
   print('Game continues.')