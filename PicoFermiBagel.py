#Pankaj Jagadale CSE
import random
def randomNum():
    while(True):
        random_number = random.randint(100, 999)
        digits = [int(digit) for digit in str(random_number)]
        if len(digits) == len(set(digits)):
            return random_number
realNum = randomNum()
rlist = []
demo = realNum
while(demo!=0):
    rlist.append(demo%10)
    demo //= 10
rlist.reverse()    
count = 0 
while(count!=1):
    player = int(input("Enter your number: "))
    if(len(str(player))!=3):
        print("Enter a 3-digit number.")
        continue
    else:
        if(realNum==player):
            print("Congrats you guess the right number!🎉")
            count += 1
            break
        else:
            playerlist = []
            demo = player
            while(demo!=0):
                playerlist.append(demo%10)
                demo //= 10
            playerlist.reverse()    
            f, p = 0, 0        #Pankaj Jagadale CSE
            a1,a2,a3=rlist[0],rlist[1],rlist[2]
            b1,b2,b3=playerlist[0],playerlist[1],playerlist[2]
            c1,c2,c3=rlist.count(b1),rlist.count(b2),rlist.count(b3) #Pankaj Jagadale CSE
            if(c1>0):
                if(playerlist.index(b1)!=rlist.index(b1)):
                    p += 1
            if(c2>0):
                if(playerlist.index(b2)!=rlist.index(b2)):
                    p += 1 
            if(c3>0):
                if(playerlist.index(b3)!=rlist.index(b3)):
                    p += 1               
            for i in range(3):
                if(rlist[i]==playerlist[i]):
                    f += 1
            else:
                if(f>0 and p>0):
                    print("Feedback:",f,"fermi,",p,"pico")  
                elif(p>0):
                    print("Feedback:",p,"pico") 
                elif(f>0):
                    print("Feedback:",f,"fermi")      
                else:
                    print("Feedback: bagel")    
#Pankaj Jagadale CSE        
            
    