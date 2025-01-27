# rolling dice simulator
import random
print("welcome to rolling dice simulator")

choice = input("Want to roll the dice?(yes/no)")

while (choice== 'yes'):
    num = random.randint(1,6)

    if num==1:
        print("----------")
        print("          ")
        print("    0     ")
        print("          ")
        print("----------")
        choice = input("Want to roll the again?(yes/no)")
    elif num==2:
        print("----------")
        print("          ")
        print("    0 0   ")
        print("          ")
        print("----------")
        choice = input("Want to roll the again?(yes/no)")
    elif num==3:
         print("----------")
         print("          ")
         print("    0 0   ")
         print("     0    ")
         print("----------")
         choice = input("Want to roll the again?(yes/no)")
    elif num==4:
         print("----------")
         print("          ")
         print("    0 0   ")
         print("    0 0   ")
         print("----------")
         choice = input("Want to roll the again?(yes/no)")
    elif num==5:
         print("----------")
         print("          ")
         print("  0 0 0   ")
         print("   0 0    ")
         print("----------")
         choice = input("Want to roll the again?(yes/no)")

    else: 
         print("----------")
         print("          ")
         print("  0 0 0   ")
         print("  0 0 0   ")
         print("----------")
         choice = input("Want to roll the again?(yes/no)")
         
if (choice== 'no'):

  choice = input("okay do you want to play another game??(yes/no)")


if (choice == 'yes'):
     print(" currently  no games available try next time!")


# 28TH NOVEMBER  just fixed the dice game now its not an infinite loop anymore.