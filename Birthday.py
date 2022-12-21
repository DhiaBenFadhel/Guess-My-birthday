from time import sleep

print("*********** Welcome To: Guess my Birthday? *******************")

def Input():
    day=int(input("Enter the day number : "))
    while not(1<=day<=31):
        day=int(input("Enter the day number!! : "))
    
    month=int(input("Enter the month number : "))
    while not(1<=month<=12):
        month=int(input("Enter the month number!! : "))
    
    year=int(input("Enter the year number : "))
    while not(1900<=year<=2022):
        year=int(input("Enter the year number!! : "))
    
    #very important
    return day,month,year

def Output(d,m,y):
    print("You entered the following date: ",d,"/",m,"/",y)
    print("Now, Let's see if it is my Birthday date ?__?")
    print("Checking ........")
    sleep(1.5)
    if (d==21)and(m==12)and(y==2003):
        print("Wow It IS My birthday date :) Amazing ;D")
    else:
        print("Nope U guessed Wrong ;(")
        
#Calling the functions Input and Output
day,month,year=Input()
sleep(1)
Output(day,month,year)