grade = eval(input('Enter your score: '))
if grade>=90:
    print('A')
elif grade>=80:
    print('B')
elif grade>=70:
    print('C')
elif grade>=60:
    print('D')
else:
     print('F')

friend = input("Do you want to check your friend`s grade? ")

if friend.lower() != "yes":
     quit()
print("Okay , enter his/her score? :")

while friend.lower() !="yes":
  print("lets proceed")
grade = eval(input('Enter his/her score: '))
if grade>=90:
    print('A')
elif grade>=80:
    print('B')
elif grade>=70:
    print('C')
elif grade>=60:
    print('D')
else:
     print('F')

if friend.lower() !="yes":
    SystemExit