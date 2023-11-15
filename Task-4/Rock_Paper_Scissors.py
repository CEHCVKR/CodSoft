import random

RPS=["Rock","Paper","Scissors"]
cmp_pts=0
usr_pts=0
user_pnnts=0
usr_pnts=0
cmp_chc=""
usr_chc=""
print("5 Games will be played in this round")
print("Win atleast 3 times to go to next Round\n")
#Round-I
for i in range(5):
    print("\n\n1. Rock\n2. Paper\n3. Scissors")
    ch=int(input("Choose one: "))
    if ch==1 or ch==2 or ch==3:
        for j in range(1,4):
            if ch==j:
                usr_chc=RPS[j-1]
        cmp_chc=random.choice(RPS)
        print("\nYou have Chosen {0}".format(usr_chc))
        print("Computer has Chosen {0}".format(cmp_chc))
        if(usr_chc=="Rock" and cmp_chc=="Paper"):
            print("Paper wins on Rock...")
            cmp_pts=cmp_pts+1
            print("\nYour Score: {0}\nComputer Score: {1}".format(usr_pts,cmp_pts))

        elif(usr_chc=="Rock" and cmp_chc=="Scissors"):
            print("Rock wins on Scissors...")
            usr_pts=usr_pts+1
            print("\nYour Score: {0}\nComputer Score: {1}".format(usr_pts,cmp_pts))

        elif(usr_chc=="Paper" and cmp_chc=="Rock"):
            print("Paper wins on Rock...")
            usr_pts=usr_pts+1
            print("\nYour Score: {0}\nComputer Score: {1}".format(usr_pts,cmp_pts))

        elif(usr_chc=="Paper" and cmp_chc=="Scissors"):
            print("Scissors wins on Paper...")
            cmp_pts=cmp_pts+1
            print("\nYour Score: {0}\nComputer Score: {1}".format(usr_pts,cmp_pts))

        elif(usr_chc=="Scissors" and cmp_chc=="Rock"):
            print("Rock wins on Scissors...")
            cmp_pts=cmp_pts+1
            print("\nYour Score: {0}\nComputer Score: {1}".format(usr_pts,cmp_pts))

        elif(usr_chc=="Scissors" and cmp_chc=="Paper"):
            print("Scissors wins on Paper...")
            usr_pts=usr_pts+1
            print("\nYour Score: {0}\nComputer Score: {1}".format(usr_pts,cmp_pts))

        elif(usr_chc=="Rock" and cmp_chc=="Rock"):
            print("Both have chosen Rock...")
            #usr_pts=usr_pts+1
            #cmp_pts=cmp_pts+1
            print("\nYour Score: {0}\nComputer Score: {1}".format(usr_pts,cmp_pts))

        elif(usr_chc=="Scissors" and cmp_chc=="Scissors"):
            print("Both have chosen Scissors...")
            #usr_pts=usr_pts+1
            #cmp_pts=cmp_pts+1
            print("\nYour Score: {0}\nComputer Score: {1}".format(usr_pts,cmp_pts))

        elif(usr_chc=="Paper" and cmp_chc=="Paper"):
            print("Both have chosen Paper...")
            #usr_pts=usr_pts+1
            #cmp_pts=cmp_pts+1
            print("\nYour Score: {0}\nComputer Score: {1}".format(usr_pts,cmp_pts))
user_ptss=usr_pts


if(user_ptss>=3):
    print("\n\nCongratulations, You are qualified to Round-II")
    print("3 Games will be layed in this round")
    print("Win atleast twice to qualify to next round")
    cmp_pts=0
    user_pnnts=0
    cmp_chc=""
    usr_chc=""
    for i in range(3):
        print("\n\n1. Rock\n2. Paper\n3. Scissors")
        ch=int(input("Choose one: "))
        if ch==1 or ch==2 or ch==3:
            for j in range(1,4):
                if ch==j:
                    usr_chc=RPS[j-1]
            cmp_chc=random.choice(RPS)
            print("\nYou have Chosen {0}".format(usr_chc))
            print("Computer has Chosen {0}".format(cmp_chc))
            if(usr_chc=="Rock" and cmp_chc=="Paper"):
                print("Paper wins on Rock...")
                cmp_pts=cmp_pts+1
                print("\nYour Score: {0}\nComputer Score: {1}".format(user_pnnts,cmp_pts))

            elif(usr_chc=="Rock" and cmp_chc=="Scissors"):
                print("Rock wins on Scissors...")
                user_pnnts=user_pnnts+1
                print("\nYour Score: {0}\nComputer Score: {1}".format(user_pnnts,cmp_pts))

            elif(usr_chc=="Paper" and cmp_chc=="Rock"):
                print("Paper wins on Rock...")
                user_pnnts=user_pnnts+1
                print("\nYour Score: {0}\nComputer Score: {1}".format(user_pnnts,cmp_pts))

            elif(usr_chc=="Paper" and cmp_chc=="Scissors"):
                print("Scissors wins on Paper...")
                cmp_pts=cmp_pts+1
                print("\nYour Score: {0}\nComputer Score: {1}".format(user_pnnts,cmp_pts))

            elif(usr_chc=="Scissors" and cmp_chc=="Rock"):
                print("Rock wins on Scissors...")
                cmp_pts=cmp_pts+1
                print("\nYour Score: {0}\nComputer Score: {1}".format(user_pnnts,cmp_pts))

            elif(usr_chc=="Scissors" and cmp_chc=="Paper"):
                print("Scissors wins on Paper...")
                user_pnnts=user_pnnts+1
                print("\nYour Score: {0}\nComputer Score: {1}".format(user_pnnts,cmp_pts))

            elif(usr_chc=="Rock" and cmp_chc=="Rock"):
                print("Both have chosen Rock...")
                #user_pnnts=user_pnnts+1
                #cmp_pts=cmp_pts+1
                print("\nYour Score: {0}\nComputer Score: {1}".format(user_pnnts,cmp_pts))

            elif(usr_chc=="Scissors" and cmp_chc=="Scissors"):
                print("Both have chosen Scissors...")
                #user_pnnts=user_pnnts+1
                #cmp_pts=cmp_pts+1
                print("\nYour Score: {0}\nComputer Score: {1}".format(user_pnnts,cmp_pts))

            elif(usr_chc=="Paper" and cmp_chc=="Paper"):
                print("Both have chosen Paper...")
                #user_pnnts=user_pnnts+1
                #cmp_pts=cmp_pts+1
                print("\nYour Score: {0}\nComputer Score: {1}".format(user_pnnts,cmp_pts))
elif(user_ptss<=3):
    print("You have performed well\nBetter Luck Next Time!!!")
user_pnts=user_pnnts



if(user_pnts>=2):
    print("\n\nCongratulations, You are qualified to Round-III")
    print("1 Games will be played in this round")
    print("Win 1 Game to become Winner")
    cmp_pts=0
    usr_pnts=0
    cmp_chc=""
    usr_chc=""
    for i in range(1):
        print("\n\n1. Rock\n2. Paper\n3. Scissors")
        ch=int(input("Choose one: "))
        if ch==1 or ch==2 or ch==3:
            for j in range(1,4):
                if ch==j:
                    usr_chc=RPS[j-1]
            cmp_chc=random.choice(RPS)
            print("\nYou have Chosen {0}".format(usr_chc))
            print("Computer has Chosen {0}".format(cmp_chc))
            if(usr_chc=="Rock" and cmp_chc=="Paper"):
                print("Paper wins on Rock...")
                cmp_pts=cmp_pts+1
                print("\nYour Score: {0}\nComputer Score: {1}".format(usr_pnts,cmp_pts))

            elif(usr_chc=="Rock" and cmp_chc=="Scissors"):
                print("Rock wins on Scissors...")
                usr_pnts=usr_pnts+1
                print("\nYour Score: {0}\nComputer Score: {1}".format(usr_pnts,cmp_pts))

            elif(usr_chc=="Paper" and cmp_chc=="Rock"):
                print("Paper wins on Rock...")
                usr_pnts=usr_pnts+1
                print("\nYour Score: {0}\nComputer Score: {1}".format(usr_pnts,cmp_pts))

            elif(usr_chc=="Paper" and cmp_chc=="Scissors"):
                print("Scissors wins on Paper...")
                cmp_pts=cmp_pts+1
                print("\nYour Score: {0}\nComputer Score: {1}".format(usr_pnts,cmp_pts))

            elif(usr_chc=="Scissors" and cmp_chc=="Rock"):
                print("Rock wins on Scissors...")
                cmp_pts=cmp_pts+1
                print("\nYour Score: {0}\nComputer Score: {1}".format(usr_pnts,cmp_pts))

            elif(usr_chc=="Scissors" and cmp_chc=="Paper"):
                print("Scissors wins on Paper...")
                usr_pnts=usr_pnts+1
                print("\nYour Score: {0}\nComputer Score: {1}".format(usr_pnts,cmp_pts))

            elif(usr_chc=="Rock" and cmp_chc=="Rock"):
                print("Both have chosen Rock...")
                #usr_pnts=usr_pnts+1
                #cmp_pts=cmp_pts+1
                print("\nYour Score: {0}\nComputer Score: {1}".format(usr_pnts,cmp_pts))

            elif(usr_chc=="Scissors" and cmp_chc=="Scissors"):
                print("Both have chosen Scissors...")
                #usr_pnts=usr_pnts+1
                #cmp_pts=cmp_pts+1
                print("\nYour Score: {0}\nComputer Score: {1}".format(usr_pnts,cmp_pts))

            elif(usr_chc=="Paper" and cmp_chc=="Paper"):
                print("Both have chosen Paper...")
                #usr_pnts=usr_pnts+1
                #cmp_pts=cmp_pts+1
                print("\nYour Score: {0}\nComputer Score: {1}".format(usr_pnts,cmp_pts))
    if(usr_pnts==1):
        print("Congratulations!!! You've finished the game")
    else:
        print("You have performed well\nBetter Luck Next Time!!!")
else:
    print("You have performed well\nBetter Luck Next Time!!!")
