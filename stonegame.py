import random
a=["STONE","PAPER","SEIOSSER"]
 

while True:
 ccount=0
 ucount=0
 userchoice=int((input( '''    
             -GAME

        PRESS-1 TO START

        PRESS-0 TO EXIT '''

 )))

 if userchoice==1:
    for x in range(1,6):
          userinput=int(input(''' 
               1- STONE
               2- PAPER
               3- SEIOSSER 
           '''))
          if userinput==1:
           yourchoice="STONE"
          elif userinput==2:
            yourchoice="PAPER"
          elif userinput==3:
            yourchoice="SEIOSSER"
          cchoice=random.choice(a)
          if yourchoice==cchoice:
           print("COMPUTER CHOICE--",cchoice)
           print('YOUR CHOICE--',yourchoice)
           print("GAME DRAW")
           ccount= ccount+1
           ucount= ucount+1
          elif yourchoice=="STONE"and cchoice=="PAPER":
           print("COMPUTER CHOICE--",cchoice)
           print('YOUR CHOICE--',yourchoice)
           print("YOU LOSS")
           ccount=ccount+1
           
          
          elif yourchoice=="STONE"and cchoice=="SEIOSSER":
           print("COMPUTER CHOICE--",cchoice)
           print('YOUR CHOICE--',yourchoice)
           print("YOU WIN")
           ucount=ucount+1
           
          elif yourchoice=="PAPER"and cchoice=="STONE":
           print("COMPUTER CHOICE--",cchoice)
           print('YOUR CHOICE--',yourchoice)
           print("YOU WIN")
           ucount=ucount+1

          elif yourchoice=="PAPER"and cchoice=="SEIOSSER":
           print("COMPUTER CHOICE--",cchoice)
           print('YOUR CHOICE--',yourchoice)
           print("YOU LOSS")
           ccount=ccount+1
          elif yourchoice=="SEIOSSER"and cchoice=="STONE":
           print("COMPUTER CHOICE--",cchoice)
           print('YOUR CHOICE--',yourchoice)
           print("YOU LOSS")
           ccount=ccount+1
          elif yourchoice=="SEIOSSER"and cchoice=="PAPER":
           print("COMPUTER CHOICE--",cchoice)
           print('YOUR CHOICE--',yourchoice)
           print("YOU WIN")
           ucount=ucount+1
          print("                           YOUR SCORE",ucount)
          print('                           COMPUTER SCORE',ccount)
    if ucount==ccount:
            print("                         MATCH DRAW")
    elif ucount>ccount:
            print("                            YOU WIN")
    elif ucount<ccount:
            print("                           YOU LOSS")


 elif userchoice==0:
  break;
 else : 
        print("INVALID INPUT")
    