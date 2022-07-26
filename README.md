# oop


import time
class Atm:
    counter=1
    t=time.localtime=time.asctime(time.localtime(time.time()))
    def __init__(self):
        self.__pin=""
        self.__balance=0
        self.id=Atm.counter
        Atm.counter=Atm.counter+1
        self.manu()
    def manu(self):
        user_choice=input('''
                             ENTER 0 FOR CHOOSE OPTION FOR CARD OR THUMB
                             ENTER 1 FOR CREATE PIN
                             ENTER 2 FOR DEPOSIT AMOUNT
                             ENTER 3 FOR WITHDRAW AMOUNT
                             ENTER 4 FOR CHECK BALANCE
                             ENTER 5 FOR CHANGE YOUR PIN
                             ENTER 6 FOR CHECK YOUR ACCOUNT NUMBER
                             ENTER 7 FOR EXIT
                             ENTER ABOVE ANY NUMBER FOR YOUR PORPOSE
                             ''')
        if user_choice=="0":
            self.option()
        elif user_choice=="1":
            self.create_pin()
        elif user_choice=="2":
            self.deposit()
        elif user_choice=="3":
            self.withdraw()
        elif user_choice=="4":
            self.check_balance()
        elif user_choice=="6":
            self.check_id()
        elif user_choice=="7":
            print("THANKS")
        
        elif user_choice=="5":
            self.change_pin()
    def check_id(self):
        temp=input("ENTER YOUR PIN\n")
        if temp==self.__pin:
            print("YOUR ID NUMBER IS : ",Atm.counter)
            self.manu()
        else:
            print("INVALID PIN")
    def option(self):
        option=int(input("HERE YOU HAVE TWO OPTION 1 FOR ATM CARD 2 FOR THUMB\n"))
        if option==1:
                print("CARD SUCCESSFULLY SCANED")
                self.manu()
        elif option==2:
                print("THUMB SUCCESSFULLY SCANED")
                self.manu()
        else:
            print("INVALID OPTION")
    def create_pin(self):
        self.__pin=input("ENTER YOUR PIN\n")
        print("SUCCESSFULLY PIN CREATED")
        self.manu()
    def change_pin(self):
        temp=input("ENTER YOUR OLD PIN\n")
        if temp==self.__pin:
            new=input("ENTER NEW PIN\n")
            newconfrem=input("ENTER CONFERM PIN\n")
            if new==newconfrem:
                self.__pin=new
                print("SUCCESSFULLY CHANGED")
                self.manu()
            else:
                print("SOMETHING WENT WRONG")
        else:
            print("INVALID PIN")
    def deposit(self):
        temp=input("ENTER YOUR PIN\n")
        if temp==self.__pin:
            deposit_amount=int(input("ENTER THE AMOUNT YOU WANT TO DEPOSIT\n"))
            self.__balance=self.__balance+deposit_amount
            print("SUCCESSFULLY DEPOSIT")
            userslip=input("YOU ARE WANT TO GET SLIP IF YES PRESS Y,y IF NO PRESS N,n\n")
            if userslip=="Y" or userslip=="y":
              print("DATE AND TIME  :  ",Atm.t)
              print("YOU DEPOSIT AMOUNT  :  ",deposit_amount)
              print("YOUR AVAIABLE BALANCE  :  ",self.__balance)
            elif userslip=="N" or userslip=="n":
              print("THANK YOU")
              
        
            self.manu()
        else:
            print("INVALID PIN")
    def withdraw(self):
        temp=input("ENTER YOUR PIN\n")
        if temp==self.__pin:
            withdraw_amount=int(input("ENTER WITHDRAW AMOUNT\n"))
            if withdraw_amount<=self.__balance:
                self.__balance=self.__balance-withdraw_amount
                print("SUCCESSFULLY DEPOSIT")
                userslip=input("YOU ARE WANT TO GET SLIP IF YES PRESS Y,y IF NO PRESS N,n\n")
                if userslip=="Y" or userslip=="y":
                  print("DATE AND TIME  :  ",Atm.t)
                  print("YOU WITHDRAW AMOUNT  :  ",withdraw_amount)
                  print("YOUR AVAIABLE BALANCE  :  ",self.__balance)
                elif userslip=="N" or userslip=="n":
                    print("THANK YOU")
                self.manu()
            else:
                print("INCUFICIENT BALANCE")
        else:
            print("INVALID PIN")
    def check_balance(self):
        temp=input("ENTER YOUR PIN\n")
        if temp==self.__pin:
            print("TOUR BALANCE IS ",self.__balance)
            self.manu()
        else:
            print("INVALID PIN")
arslan=Atm()
usman=Atm()
naeem=Atm()
                
        
